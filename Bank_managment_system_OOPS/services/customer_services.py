from database.database import get_connection


class CustomerService:

    def add_customer(self, customer):
        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO customers
            (customer_id, name, phone, email, address)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                customer.customer_id,
                customer.name,
                customer.phone,
                customer.email,
                customer.address
            )

            cursor.execute(query, values)
            connection.commit()

            print("✅ Customer Added Successfully.")

        except Exception as error:
            print("Error :", error)

        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()

