from datetime import datetime
import random


from datetime import datetime

def get_current_datetime():
    return datetime.now()


def generate_transaction_id():
    number = random.randint(1000, 9999)
    transaction_id = "TXN" + str(number)
    return transaction_id
