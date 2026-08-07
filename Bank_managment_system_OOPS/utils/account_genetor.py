import random
def generate_account_number():
    number = random.randint(1000, 9999)

    account_number = "ACC" + str(number)
    return account_number



