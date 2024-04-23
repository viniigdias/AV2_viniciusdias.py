# Definição dos dicionários de usuários e contas usando expressões Lambda.
get_user_accounts = lambda: {
    'user1': {'account_balance': 1000, 'password': 'pass1'},
    'user2': {'account_balance': 2000, 'password': 'pass2'},
}

# Simulação de uma função que atualiza o saldo da conta
update_account_balance = lambda accounts, user_id, amount: {
    **accounts,
    user_id: {
        **accounts[user_id],
        'account_balance': accounts[user_id]['account_balance'] - amount
    }
}

# Simulação de uma função que completa uma transação
complete_transaction = lambda accounts, user_id: (
    "Transação completa",
    update_account_balance(accounts, user_id, 0) # Simula a finalização sem alterar o saldo
)

# Simulação de uma função que fecha uma transação
close_transaction = lambda: "Transação fechada"

# Simulação de uma função que cancela uma transação
cancel_transaction = lambda: "Transação cancelada"

# Processamento de transações em dinheiro
process_dinheiro_transaction = lambda accounts, user_id, amount: (
    "Transação completa",
    update_account_balance(accounts, user_id, amount)
)

# Processamento de transações de transferenciaência
confirm_payment_approval = lambda: True # Simulação de confirmação de pagamento
process_transferencia_transaction = lambda accounts, user_id, amount: (
    complete_transaction(accounts, user_id) if confirm_payment_approval() else cancel_transaction()
)

# Função para criar uma transação
create_transaction = lambda user_id, transaction_type, amount: (
    "Usuario não encontrado" if user_id not in get_user_accounts() else
    "Tipo de transação invalida" if transaction_type not in ['dinheiro', 'transferencia'] else
    process_dinheiro_transaction(get_user_accounts(), user_id, amount) if transaction_type == 'dinheiro' else
    process_transferencia_transaction(get_user_accounts(), user_id, amount) if transaction_type == 'transferencia' else
    "Tipo de transação invalida"
)

# Exemplo de uso:
user_id = 'user2'
transaction_type = 'dinheiro'
amount = 200

# Criação e processamento de uma transação
transaction_result = create_transaction(user_id, transaction_type, amount)
print(transaction_result)
