import json
from typing import Literal, Union
import random

# TODO: Card() class

# Account Classes =================================================================================
class Account:
    """Creates a new account"""
    def __init__(self, name: str, account_no: int, pin: int, balance: float):
        self.name = name.capitalize()
        self.account_no = account_no
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return f"""{self.name}'s balance: {self.balance}"""

class NewAccount(Account):
    def __init__(self, name: str, pin: int):
        self.account_no = generateAccountNumber()
        super().__init__(name, self.account_no, pin, 0)
        _update_ledger(self)

class ExistingAccount(Account):
    def __init__(self, account_no: int, pin: int):
        customer = _readLedgers()[str(account_no)]
        name = customer["name"]
        balance = customer["balance"]
        super().__init__(name, account_no, pin, balance)




# Transactions ====================================================================================
class Operations:
    """Does different operations on the account given in initiation."""
    def __init__(self, account:Account):
        self.account = account

    def checkBalance(self) -> float:
        """Returns the balance in account"""
        with open("_ledgers.json", "r") as fp:
            customers = json.load(fp)
        return customers[self.account.account_no]["balance"]

    def withdraw(self, amount:float) -> float:
        """Subtracts the amount from balance and returns the new balance."""
        self.account.balance -= amount
        _update_ledger(self.account)
        return self.account.balance

    def deposit(self, amount:float) -> float:
        """Adds the amount to balance and returns the new balance."""
        self.account.balance += amount
        _update_ledger(self.account)
        return self.account.balance


# Functions =======================================================================================
def _readLedgers() -> dict:
    """Returns the contents of '_ledgers.json'"""
    with open("_ledgers.json", "r+") as fp:
        customers = json.load(fp)
    return customers

def _update_ledger(account:Account) -> None:
    """Updates the details of the given account in '_ledgers.json'."""
    # Gets the current ledgers
    customers = _readLedgers()
    # Make the change.
    customers[account.account_no] = account.__dict__
    # Updates the ledgers
    with open("_ledgers.json", "w") as fp:
        json.dump(customers, fp, indent=2)  # type: ignore

def generateAccountNumber() -> int:
    """Generates and returns new and original a 9-digit account number,
    and adds it to 'account_numbers.json'"""

    # Read
    with open("account_numbers.json", "r") as fp:
        account_nums = eval(fp.read())

    # Generate number
    acc_no = account_nums[0]
    while acc_no in account_nums:
        acc_no = random.randint(100_000_000, 999_999_999)
    account_nums.append(acc_no)

    # Write generated number
    with open("account_numbers.json", "w") as fp:
        json.dump(account_nums, fp)  # type: ignore

    return acc_no

def checkValidAccountNo(account_no: int) -> bool:
    """Returns False if account_no is wrong, True if everything matches."""
    with open("_ledgers.json", "r") as fp:
        customers = json.load(fp)

    return str(account_no) in customers

def checkValidPin(account_no: Union[int|str],  pin: int) -> bool:
    """Returns False if pin is wrong, True if everything matches."""
    with open("_ledgers.json", "r") as fp:
        customers = json.load(fp)

    acc = customers[str(account_no)]
    validPin = acc["pin"]
    return True if pin == validPin else False

