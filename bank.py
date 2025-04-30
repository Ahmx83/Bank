import json
from typing import TextIO


class Account:
    """Creates a new account"""
    def __init__(self, name: str, account_no: int, pin: int, balance: float):
        self.name = name.capitalize()
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
        self._update_ledger()

    def _update_ledger(self):
        # Gets the current ledgers
        with open("ledgers.json", "r") as fp:
            customers = json.load(fp)
        # Updates the ledgers
        with open("ledgers.json", "w") as fp: # type: TextIO
            customers[self.name] = self.__dict__
            json.dump(customers, fp, indent=2)

class Operations:
    """Does different operations on the account given in initiation."""
    def __init__(self, account:Account):
        self.account = account

    def CheckBalance(self) -> float:
        """Returns the balance in account"""
        with open("ledgers.json", "r") as fp:
            customers = json.load(fp)
        return customers[self.account.name]["balance"]

    def withdraw(self, amount:float) -> float:
        """Subtracts the amount from balance and returns the new balance."""
        self.account.balance -= amount
        return self.account.balance

    def deposit(self, amount:float) -> float:
        """Adds the amount to balance and returns the new balance."""
        self.account.balance += amount
        return self.account.balance


