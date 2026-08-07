from decimal import Decimal
from database.database import get_connection
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from services.transaction_services import TransactionService
from utils.account_genetor import generate_account_number
from utils.validator import validate_amount
from exception.custom_exception import (
    InvalidAmountError,
    InsufficientBalanceError,
    AccountNotFoundError,
    CustomerNotFoundError,
    InvalidAccountTypeError
    
)

class AccountService:
    def createAccount(
            self,
            customer_id,
            account_type,
            balance,
            interest_rate=None,
            overdraft_limit=None
    ):
        balance = float(balance)
        if not validate_amount(balance):
            raise InvalidAmountError()
        if account_type.lower() not in ["savings", "current"]:
            raise InvalidAccountTypeError()

        account_number = generate_account_number()
        connection = None
        cursor = None

        try:
             connection = get_connection()
             cursor = connection.cursor()

             query = """
            INSERT INTO accounts
            (
                account_number,
                customer_id,
                balance,
                account_type,
                interest_rate,
                overdraft_limit
            )
            VALUES
            (%s, %s, %s, %s, %s, %s)
            """

             values = (
                account_number,
                customer_id,
                balance,
                account_type,
                interest_rate,
                overdraft_limit
            )

             cursor.execute(query, values)
             connection.commit()

             print("Account created successfully....")
             print("Account Number :", account_number)


        except Exception as error:
            print("Error", error)

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()


#---------------------------------------Deposit---------------------------------------

    def deposit(self, account_number, amount):
        try:
            amount = Decimal(str(amount))
        except (TypeError, ValueError, ArithmeticError):
            raise InvalidAmountError("Amount must be a valid number")

        if not validate_amount(amount):
            raise InvalidAmountError()

        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            SELECT balance
            FROM accounts
            WHERE account_number = %s
            """

            cursor.execute(query, (account_number.strip(),))
            result = cursor.fetchone()

            if result is None:
                raise AccountNotFoundError("User Account is not found")

            current_balance = Decimal(str(result[0]))
            new_balance = current_balance + amount

            update_query = """
            UPDATE accounts
            SET balance = %s
            WHERE account_number = %s
            """

            cursor.execute(update_query, (new_balance, account_number.strip()))
            connection.commit()

            transaction_service = TransactionService()
            transaction_service.add_transaction(
                account_number.strip(),
                "Deposit",
                amount
            )

            print("Deposit Successfully......")
            print("Updated Balance :", new_balance)

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


# -----------------------------------Withdraw----------------------------------

    def withdraw(self, account_number, amount):
        try:
            amount = Decimal(str(amount))
        except (TypeError, ValueError, ArithmeticError):
            raise InvalidAmountError("Amount must be a valid number")

        if not validate_amount(amount):
            raise InsufficientBalanceError("Amount must be greater than zero")

        connection = None
        cursor = None
        transaction_service = TransactionService()

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            SELECT balance
            FROM accounts
            WHERE account_number = %s
            """
            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result is None:
                raise AccountNotFoundError()

            current_balance = Decimal(str(result[0]))

            if amount > current_balance:
                raise InsufficientBalanceError("Insufficient Balance")

            new_balance = current_balance - amount

            update_query = """
            update accounts 
            set balance = %s 
            where account_number = %s
            """
            cursor.execute(update_query, (new_balance, account_number))
            connection.commit()

            transaction_service = TransactionService()
            transaction_service.add_transaction(
            account_number,
            "Withdraw",
            amount
            )

            print("Withdraw Successfully......")
            print("Updated Balance :", new_balance)  

        except Exception as error:
            print("Error :", error)
            return None

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


# -------------------------------Search account----------------------------------------

    def search(self, account_number):
        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            select * from accounts 
            where account_number = %s
            """

            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result is None:
                raise AccountNotFoundError()

            print("Account Found....")
            print(result)
            return result

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

# ------------------------------Display details------------------------------------


    def display_account(self, account_number):
        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            select * from accounts
            where account_number = %s
            """
            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result is None:
                raise AccountNotFoundError()\

            print("-------------------Account Details------------------")
            print("Account Number        :", result[0])
            print("Customer_ID           :", result[1])
            print("Balance               :", result[2])
            print("Account type          :", result[3])
            print("Interest Rate         :", result[4])
            print("Overdraft limit       :", result[5])

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


# ------------------------------Update Account details--------------------------------

    def update_account(self, account_number, interest_rate, overdraft_limit):
        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            select account_number from 
            accounts where account_number = %s
            """

            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result is None:
                raise AccountNotFoundError()

            update_query = """
            update accounts set 
            interest_rate = %s,
            overdraft_limit = %s
            where account_number = %s
            """

            cursor.execute(update_query, (interest_rate, overdraft_limit, account_number))

            connection.commit()

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


# ---------------------------------Delete Accounts---------------------------------

    def delete_account(self, account_number):
        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            select account_number
            from accounts where
            account_number = %s
            """

            cursor.execute(query, (account_number,))\

            result = cursor.fetchone()
            if result is None:
                raise AccountNotFoundError()

            delete_query = """
            delete from accounts 
            where account_number = %s
            """
            cursor.execute(delete_query, (account_number,))

            connection.commit()

            print("Account Deleted Successfully....")

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

