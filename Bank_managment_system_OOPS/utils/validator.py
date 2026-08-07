def validate_amount(amount):
    if amount > 0:
        return True
    else:
        return False
def validate_phone(phone):
    phone = str(phone)

    if len(phone) == 10 and phone.isdigit():
        return True
    else:
        return False

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        False 
def validate_account_type(account_type):
    if account_type.lower() == "savings" or account_type.lower() == "current":
        return True
    else:
        return False    

def validate_name(name):
    if name.replace(" ", "").isalpha():
        return True
    else:
        return False
