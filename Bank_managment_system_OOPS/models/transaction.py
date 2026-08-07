class Transaction:
    def __init__(self, transaction_id, account_number,transaction_type, amount, date, time):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type =transaction_type
        self.amount = amount
        self.date = date
        self.time = time

    def display_transaction(self):
        print("----------------------Transaction Receipt------------------------")
        print("Transaction ID   :", self.transaction_id)
        print("Account Number   :", self.account_number)
        print("transaction_type :", self.transaction_type)
        print("Amount           :", self.amount)
        print("Date             :", self.date)
        print("Time             :", self.time)
