import json
import operator
from typing import Union
import random

# TODO: combine Account() & Operators()
# TODO: Card() class

# Account Classes =================================================================================
# TODO: Account() should be able to deal with invalid input
class AccountException(Exception):
    """This account module raises this when the module is misused."""
    pass

class Account:
    """Creates a new account"""
    def __init__(self, name: str, account_no: int|str,
                 pin: int|str, balance: float|str):
        try:
            self.name = name.capitalize()
            self.account_no = int(account_no)
            self.pin = int(pin)
            self._balance = float(balance)
        except ValueError:
            raise AccountException("Invalid data type entered.")
        except AttributeError:
            raise AccountException("'name' must be an instance of str.")

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount:float) -> float:
        """Subtracts the amount from balance and returns the new balance."""
        if amount > self.balance:
            raise AccountException(
            "The amount you are trying to withdraw is greater than your current balance."
            )
        self._balance -= amount
        self._update_ledger()
        return self._balance

    def deposit(self, amount:float) -> float:
        """Adds the amount to balance and returns the new balance."""
        self._balance += amount
        self._update_ledger()
        return self._balance

    def __str__(self):
        return f"{self.name}'s balance: ${self._balance:.2f}"

    def __repr__(self):
        cls = self.__class__.__qualname__
        return (f"{cls}(name={self.name}, account_no={self.account_no}, "
                f"pin={'*'*4}, balance={self.balance:.2f})")

    def _comparisonOperatorHelper(self, operator_func, other):
        """A helper method for our comparison dunder methods"""
        if isinstance(other, Account):
            return operator_func(self.balance)
        elif isinstance(other, (int, float)):
            return operator_func(self.balance, other)
        elif operator_func == operator.eq:
            return False
        elif operator_func == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):
        return self._comparisonOperatorHelper(operator.eq, other)

    def __ne__(self, other):
        return self._comparisonOperatorHelper(operator.ne, other)

    def __gt__(self, other):
        return self._comparisonOperatorHelper(operator.gt, other)

    def __ge__(self, other):
        return self._comparisonOperatorHelper(operator.ge, other)

    def __lt__(self, other):
        return self._comparisonOperatorHelper(operator.lt, other)

    def __le__(self, other):
        return self._comparisonOperatorHelper(operator.le, other)

    @staticmethod
    def _readLedgers() -> dict:
        """Returns the contents of '_ledgers.json'"""
        with open("_ledgers.json", "r+") as fp:
            customers = json.load(fp)
        return customers

    def _update_ledger(self) -> None:
        """Updates the details of the account in '_ledgers.json'."""
        # Gets the current ledgers
        customers = self._readLedgers()
        # Make the change.
        customer_data = customers[str(self.account_no)]
        customer_data.update(self.__dict__)

        # Updates the ledgers
        with open("_ledgers.json", "w") as fp:
            json.dump(customers, fp, indent=2)  # type: ignore


class NewAccount(Account):
    def __init__(self, name: str, pin: int):
        self.account_no = generateAccountNumber()
        super().__init__(name, self.account_no, pin, 0)
        self._update_ledger()

class ExistingAccount(Account):
    def __init__(self, account_no: int, pin: int):
        customer = self._readLedgers()[str(account_no)]
        name = customer["name"]
        balance = customer["_balance"]
        super().__init__(name, account_no, pin, balance)


# Functions =======================================================================================
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

def generatePin() -> int:
    """Returns a random 4-digit number for new accounts."""
    return random.randint(1000, 9999)

def checkAccountNo(account_no: int) -> bool:
    """Returns False if account_no is wrong, True if everything matches."""
    with open("_ledgers.json", "r") as fp:
        customers = json.load(fp)

    return str(account_no) in customers

def checkPin(account_no: Union[int|str],  pin: int) -> bool:
    """Returns False if pin is wrong, True if everything matches."""
    with open("_ledgers.json", "r") as fp:
        customers = json.load(fp)

    acc = customers[str(account_no)]
    validPin = acc["pin"]
    return True if pin == validPin else False