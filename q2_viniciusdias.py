import unittest
import q1_viniciusdias

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.user_accounts = lambda: {
            'user1': {'account_balance': 1000, 'password': 'pass1'},
            'user2': {'account_balance': 2000, 'password': 'pass2'},
        }

    test_cash_transaction_success = lambda self: self.assertEqual(q1_viniciusdias.create_transaction('user2', 'cash', 200)[0], "Transação completa")

    test_transfer_transaction_success = lambda self: self.assertEqual(q1_viniciusdias.create_transaction('user2', 'transfer', 200)[0], "Transação completa")

    test_invalid_user = lambda self: self.assertEqual(q1_viniciusdias.create_transaction('user3', 'cash', 200), "Usuario não encontrado")

    def test_stress(self):
        stress_test = lambda: [self.assertEqual(q1_viniciusdias.create_transaction('user1', 'cash', 10)[0], "Transação completa") for _ in range(1000)]
        stress_test()

if __name__ == '__main__':
    unittest.main()
