class Customer:
    def __init__(self, customer_id, name, phone, email, address):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display_customer(self):
        print("-----------------Customer Display---------------------")
        print("Customer_id   :", self.customer_id)
        print("Name          :", self.name)
        print("Phone         :", self.phone)
        print("Email         :", self.email)
        print("Address       :", self.address)
        