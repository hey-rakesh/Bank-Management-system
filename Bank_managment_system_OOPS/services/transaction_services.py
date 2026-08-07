from database.database import get_connection
from models.transaction import Transaction
from utils.helper import generate_transaction_id, get_current_datetime


class TransactionService:
    def _get_transaction_table_name(self, cursor):
        for table_name in ("transactions", "transaction"):
            cursor.execute("SHOW TABLES LIKE %s", (table_name,))
            if cursor.fetchone():
                return table_name
        return None

    def _ensure_transaction_table(self, cursor):
        table_name = self._get_transaction_table_name(cursor)
        if table_name:
            return table_name

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id VARCHAR(50) PRIMARY KEY,
                account_number VARCHAR(50) NOT NULL,
                transaction_type VARCHAR(20) NOT NULL,
                amount DECIMAL(12,2) NOT NULL,
                date_time DATETIME NOT NULL
            )
            """
        )
        return "transactions"

    def add_transaction(self, account_number, transaction_type, amount):
        connection = None
        cursor = None

        try:
            transaction_id = generate_transaction_id()
            date_time = get_current_datetime()
            connection = get_connection()
            cursor = connection.cursor()

            table_name = self._ensure_transaction_table(cursor)

            query = f"""
            INSERT INTO {table_name}
            (transaction_id,
            account_number,
            transaction_type,
            amount,
            date_time)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                transaction_id,
                account_number,
                transaction_type,
                amount,
                date_time,
            )
            cursor.execute(query, values)

            connection.commit()
            print("Transaction saved Successfully......")

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


# ---------------------------------Display transaction-------------------------------------

    def display_transactions(self, account_number):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()

            table_name = self._ensure_transaction_table(cursor)

            query = f"""
            select * from {table_name}
            where account_number = %s
            """
            cursor.execute(query, (account_number,))
            result = cursor.fetchall()

            if len(result) == 0:
                print("No Transaction Found........")
                return
            print("\n ----------------------------Transaction History-----------------------------")

            for transaction in result:
                print("-------------------------------------------------------")
                print("Transaction_ID                       :", transaction[0])
                print("Account Number                       :", transaction[1])
                print("Type                                 :", transaction[2])
                print("Amount                               :", transaction[3])
                print("Date & Time                          :", transaction[4])

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

            