import json
from typing import TextIO
import random

# Account Classes =================================================================================
class Account:
    """Creates a new account"""
    def __init__(self, name: str, account_no: int, pin: int, balance: float):
        self.name = name.capitalize()
        self.account_no = str(account_no)
        self.pin = pin
        self.balance = balance

class NewAccount(Account):
    def __init__(self, name: str, pin: int):
        self.account_no = generateAccountNumber()
        super().__init__(name, self.account_no, pin, 0)
        _update_ledger(self)

# class ExistingAccount(Account):
#     def __init__(self, account_no, pin):
#         super().__init__()


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
def _update_ledger(account:Account) -> None:
    # Gets the current ledgers
    with open("_ledgers.json", "r+") as fp:
        customers = json.load(fp)
    # Make the change.
    customers[account.account_no] = account.__dict__
    # Updates the ledgers
    with open("_ledgers.json", "w") as fp:
        json.dump(customers, fp, indent=2)


def getValidInput(input_, invalid_msg, *expected):
    """Keeps asking for input until given an expected input."""
    inp = input("> ")
    while inp not in expected:
        print(invalid_msg)
        inp = input("> ")
    return input_


def generateAccountNumber() -> int:
    """Generates and returns new and original a 7-digit account number."""
    with open("account_numbers.json", "r") as fp:
        account_nums = eval(fp.read())

    acc_no = 0
    while acc_no in account_nums:
        acc_no = random.randint(1_000_000, 9_999_999)

    return acc_no