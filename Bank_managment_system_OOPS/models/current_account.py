from models.bank_account import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, customer, balance, account_type, overdraft_limit):
        super().__init__(account_number, customer, balance, account_type)
        self.overdraft_limit = overdraft_limit

