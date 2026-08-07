from models.bank_account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer, balance, account_type, interest_rate):
        super().__init__(account_number, customer, balance, account_type)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        return interest
    