from typing import TypeVar
from bank import checkPin, Account, checkAccountNo

T = TypeVar('T')

def getValidInput(invalid_msg: str, *expected, key = None) -> str:
    """Keeps asking for input until given an expected input."""
    if key is None:
        key = lambda x: x

    user_input = input("> ")
    transformed_input = key(user_input)

    while transformed_input not in expected:
        print(invalid_msg)
        user_input = input("> ")
        transformed_input = key(user_input)

    return user_input

def getAccountNo() -> int:
    """Returns a valid, existing account number."""
    valid = False
    account_no = 0
    while not valid:
        account_no = getValidInput("Account numbers are 9 digits. Try again.",
                      9, key=len)
        account_no = int(account_no)
        valid = checkAccountNo(account_no)
        if not valid:
            print("You've entered an invalid account number.")
    return account_no

def getPin(account_no: int) -> int:
    """Returns the right pin relative to the account_no given.
    Assumes the given account_no is valid."""
    valid = 0
    pin = 0
    while not valid:
        pin = getValidInput("Pins are 4 digits. Try again.",
                            4, key=len)
        pin = int(pin)
        valid = checkPin(account_no, pin)
        print(valid)
    return pin