import json
import random
from typing import Union
from array import array



# Functions =======================================================================================

def get_valid_input(invalid_msg: str, *expected, key = None) -> str:
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



# Account Functions ===============================================================================

def generate_account_no() -> int:
    """Generates and returns a new and original a 9-digit account number
    and adds it to 'acc_no.bin'"""

    # Read
    arr = read_acc_bin()

    # Generate number
    acc_no = arr[0]
    while acc_no in arr:
        acc_no = random.randint(100_000_000, 999_999_999)
    arr.append(acc_no)

    # Write a generated number
    with open("customers_data/acc_no.bin", "wb") as fp:
        arr.tofile(fp)

    return acc_no

def read_acc_bin() -> array:
    with open("customers_data/acc_no.bin", "rb") as fp:
        arr = array("i")
        while True:
            try:
                arr.fromfile(fp, 1)
            except EOFError:
                break
    return arr

def is_valid_acc_no(account_no: int) -> bool:
    """Returns False if account_no is wrong, True if everything matches."""
    with open("customers_data/_ledgers.json", "r") as fp:
        customers = json.load(fp)
    return str(account_no) in customers

def get_acc_no() -> int:
    """Asks user to enter an existing account number.
    Returns a valid, existing account number."""
    print("Enter your account number.")
    valid = False
    account_no = 0
    while not valid:
        account_no = get_valid_input("Account numbers are 9 digits. Try again.", 9, key=len)
        account_no = int(account_no)
        valid = is_valid_acc_no(account_no)
        if not valid:
            print("You've entered an invalid account number.")
    return account_no



# Pin Functions ===================================================================================

def generate_pin() -> int:
    """Returns a random 4-digit number for new accounts."""
    return random.randint(1000, 9999)

def is_valid_pin(account_no: Union[int|str],  pin: int) -> bool:
    """Returns False if the pin is wrong, True if everything matches."""
    with open("customers_data/_ledgers.json", "r") as fp:
        customers = json.load(fp)

    acc = customers[str(account_no)]
    validPin_ = acc["pin"]
    return True if pin == validPin_ else False

def get_pin(account_no: int) -> int:
    """Asks user to enter the right pin relative to the account_no given.
    Assumes the given account_no is valid. Returns the valid pin."""
    print("Enter your pin.")
    valid = 0
    pin = 0
    while not valid:
        pin = get_valid_input("Pins are 4 digits. Try again.", 4, key=len)
        pin = int(pin)
        valid = is_valid_pin(account_no, pin)
        if not valid:
            print("You've entered an invalid pin number.")
    return pin
