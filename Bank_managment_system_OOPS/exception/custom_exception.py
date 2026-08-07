class InsufficientBalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)
class InvalidAmountError(Exception):
    def __init__(self, message = "Amount must be greater than Zero"):
        super().__init__(message) 
class AccountNotFoundError(Exception):
    def __init__(self, message = "User Account is not found"):
        super().__init__(message) 
class CustomerNotFoundError(Exception):
    def __init__(self, message = "Customer not found"):
        super().__init__(message)
class DuplicateAccountError(Exception):
    def __init__(self, message ="Duplicate account found"):
        super().__init__(message) 
class InvalidAccountTypeError(Exception):
    def __init__(self, message = "Invalid Account Type Error"):
        super().__init__(message)