from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
import json
import q1_viniciusdias

app = Flask(__name__)

# Expressão lambda para criar dicionários de usuários e contas
hash_password = lambda password: hashlib.sha256(password.encode()).hexdigest()
get_user_accounts = lambda: {
    'user1': {'account_balance': 1000, 'password': hash_password('pass1')},
    'user2': {'account_balance': 2000, 'password': hash_password('pass2')}
}
verify_password = lambda password, hashed_password: hash_password(password) == hashed_password

# Função para conectar ao sistema de pagamento
connect_to_payment_system = lambda: True  # Função simulada para conectar ao sistema de pagamento

# Expressão lambda para processar transações em dinheiro
process_cash_transaction = lambda accounts, user_id, amount: q1_viniciusdias.update_account_balance(accounts, user_id, amount) if connect_to_payment_system() else {"Transação completa"}

# Expressão lambda para aprovar o pagamento
confirm_payment_approval = lambda: True

# Expressão lambda para processar transações de transferência
process_transfer_transaction = lambda accounts, user_id, amount: (process_cash_transaction(accounts, user_id, amount) if confirm_payment_approval() else {"Transação completa"})

# Expressão lambda para criar uma transação
create_transaction = lambda user_id, transaction_type, amount: (
    {"Usuario não encontrado"} if user_id not in get_user_accounts() else
    {"Tipo de transação invalida"} if transaction_type not in ['cash', 'transfer'] else
    (process_cash_transaction(get_user_accounts(), user_id, amount) if transaction_type == 'cash' else
    process_transfer_transaction(get_user_accounts(), user_id, amount))
)

# Função para atualizar o saldo da conta
update_account_balance = lambda accounts, user_id, amount: (
    {"Transação completa"} if user_id in accounts else
    {"Usuario não encontrado"}
)

# Função para cifrar uma mensagem utilizando AES
encrypt_message = lambda message, key, iv: AES.new(key, AES.MODE_CBC, iv).encrypt(pad(message.encode(), AES.block_size))

# Função para decifrar uma mensagem utilizando AES
decrypt_message = lambda ciphertext, key, iv: unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext), AES.block_size).decode()

# Expressão lambda para lidar com transações
handle_transaction = lambda get_json, missing_params: (
    jsonify({'result': encrypt_message(json.dumps(create_transaction(get_json().get('user_id'), get_json().get('transaction_type'), get_json().get('amount'))), get_random_bytes(16), get_random_bytes(16)).hex()})
    if not missing_params() and get_json().get('user_id') in get_user_accounts() and verify_password(get_json().get('password'), get_user_accounts()[get_json().get('user_id')]['password'])
    else jsonify({'error': 'Missing parameters'} if missing_params() else {'error': 'Authentication failed'} if get_json().get('user_id') not in get_user_accounts() or not verify_password(get_json().get('password'), get_user_accounts()[get_json().get('user_id')]['password']) else {})
)

# Definindo uma lista vazia para armazenar o histórico de transações
transaction_log = []

# Expressão lambda para registrar uma transação no histórico
log_transaction = lambda user_id, transaction_type, amount: transaction_log.append((user_id, transaction_type, amount))

# Expressão lambda para obter informações sobre transações
get_transaction_info = lambda: jsonify({'transaction_history': [{'user_id': transaction[0], 'transaction_type': transaction[1], 'amount': transaction[2]} for transaction in transaction_log]})

@app.route('/transaction', methods=['POST', 'GET'])
# A função handle_transaction foi implementada como uma expressão lambda acima
def transaction():
    return handle_transaction(request.get_json, lambda: None in (request.get_json().get('user_id'), request.get_json().get('password'), request.get_json().get('transaction_type'), request.get_json().get('amount')))

@app.route('/transaction_info', methods=['GET'])
# A função get_transaction_info foi implementada como uma expressão lambda acima
def transaction_info():
    return get_transaction_info()

if __name__ == '__main__':
    app.run(debug=True)
