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
    "Transaction completed",
    update_account_balance(accounts, user_id, 0) # Simula a finalização sem alterar o saldo
)

# Simulação de uma função que fecha uma transação
close_transaction = lambda: "Transaction closed"

# Simulação de uma função que cancela uma transação
cancel_transaction = lambda: "Transaction canceled"

# Processamento de transações em dinheiro
process_cash_transaction = lambda accounts, user_id, amount: (
    "Transaction completed",
    update_account_balance(accounts, user_id, amount)
)

# Processamento de transações de transferência
confirm_payment_approval = lambda: True # Simulação de confirmação de pagamento
process_transfer_transaction = lambda accounts, user_id, amount: (
    complete_transaction(accounts, user_id) if confirm_payment_approval() else cancel_transaction()
)

# Função para criar uma transação
create_transaction = lambda user_id, transaction_type, amount: (
    "User not found" if user_id not in get_user_accounts() else
    "Invalid transaction type" if transaction_type not in ['cash', 'transfer'] else
    process_cash_transaction(get_user_accounts(), user_id, amount) if transaction_type == 'cash' else
    process_transfer_transaction(get_user_accounts(), user_id, amount) if transaction_type == 'transfer' else
    "Invalid transaction type"
)

# Exemplo de uso:
user_id = 'user2'
transaction_type = 'cash'
amount = 200

# Criação e processamento de uma transação
transaction_result = create_transaction(user_id, transaction_type, amount)
print(transaction_result)
