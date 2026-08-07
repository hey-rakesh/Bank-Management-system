from models.customer import Customer
from services.customer_services import CustomerService
from services.account_services import AccountService
from services.transaction_services import TransactionService
from decimal import Decimal

customer_service = CustomerService()
account_service = AccountService()
transaction_service = TransactionService()

while True:
    print("===============================================================")
    print("                     BANK MANAGEMENT SYSTEM                    ")
    print("===============================================================")

    print("1. Add Customer")
    print("2. Create Customer")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Search Account")
    print("6. Display Account")
    print("7. Update Account")
    print("8. Delete Account")
    print("9. Display Transaction")
    print("10. Exit")

    try:
        choice = int(input("\n Enter Your Choice :"))

# -------------------------------Add Customer------------------------------

        if choice == 1:
            customer_id = input("Enter Customer ID :")
            name = input("Enter Name :")
            phone = int(input("Enter Phone Number :"))
            email = input("Enter email :")
            address = input("Enter Address :")

            customer = Customer(
                                customer_id,
                                name, 
                                phone,
                                email,
                                address
                                )
            customer_service.add_customer(customer)

# -------------------------------Create Account---------------------------------------

        elif choice == 2:
            customer_id = input("Enter your Customer ID :")
            account_type = input("Enter account type (Savings/Current):").strip().lower()
            balance = Decimal(input("Enter Opening Balance : "))

            if account_type == "savings":
                interest_rate = float(input("Enter Interest Rate :"))

                account_service.createAccount(
                    customer_id,
                    account_type,
                    balance,
                    interest_rate,
                    None
                )

            elif account_type == "current":
                overdraft_limit = float(input("Enter Overdraft limit :"))
                account_service.createAccount(
                    customer_id,
                    account_type,
                    balance,
                    None,
                    overdraft_limit
                )
            else:
                print("Invalid Account type")

# -------------------------------Deposit Amount------------------------------------

        elif choice == 3:
            account_number = input("Enter Your Account Number :").strip()
            amount = Decimal(input("Enter Amount : "))
            account_service.deposit(account_number, amount)

# -----------------------------Withdraw Amount-------------------------------------

        elif choice == 4:
            account_number = input("Enter Your Account Number :").strip()
            amount = Decimal(input("Enter Amount : "))
            account_service.withdraw(account_number, amount)

# -----------------------------------Search---------------------------------------
 
        elif choice == 5:
            account_number = input("Enter Your Account Number :").strip()
            account_service.search(account_number)


# -----------------------------------Display---------------------------------------

        elif choice == 6:
            account_number = input("Enter Your Account Number :").strip()
            account_service.display_account(account_number)


# -----------------------------------Update---------------------------------------

        elif choice == 7:
            account_number = input("Enter Your Account Number :")
            interest_rate = float(input("Enter Interest Rate :"))
            overdraft_limit = float(input("Enter Overdraft Limit :"))

            account_service.update_account(account_number, interest_rate, overdraft_limit)

# -----------------------------------Delete---------------------------------------

        elif choice == 8:
            account_number = input("Enter Account number :")
            account_service.delete_account(account_number)

# --------------------------------Transaction---------------------------------------


        elif choice == 9:
            account_number = input("Enter Account number :")
            transaction_service.display_transactions(account_number)

# -----------------------------------Exit---------------------------------------

        elif choice == 10:
            print("Thank You For Using Bank Management System")
            break
        else:
            print("Invalid Choice")

    except Exception as error:
        print("Error :", error)