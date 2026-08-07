from models.customer import Customer
class BankAccount:
    def __init__(self, account_number, customer, balance, account_type):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account(self):
        print("--------------------Account Details-----------------------")
        print("Account Number    :", self.account_number)
        print("Customer          :", self.customer)
        print("Balance           :", self.balance)
        print("Account  Type     :", self.account_type)

        print("\nCustomer Information")
        self.customer.display_customer()