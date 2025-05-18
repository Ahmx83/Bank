import json
import operator
from account_funcs import generateAccountNumber

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
        self.name = name.capitalize()
        self.account_no = int(account_no)
        self.pin = int(pin)
        self._balance = float(balance)

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

    # def _comparisonOperatorHelper(self, operator_func, other):
    #     """A helper method for our comparison dunder methods"""
    #     if isinstance(other, Account):
    #         return operator_func(self.balance, other.balance)
    #     elif isinstance(other, (int, float)):
    #         return operator_func(self.balance, other)
    #     elif operator_func == operator.eq:
    #         return False
    #     elif operator_func == operator.ne:
    #         return True
    #     else:
    #         return NotImplemented

    def _comparisonOperatorHelper(self, operator_func, other):
        match other:
            case Account(balance=other_balance):
                return operator_func(self.balance, other_balance)
            case int() | float():
                return operator_func(self.balance, other)
            case _:
                if operator_func == operator.eq:
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

    def __add__(self, other):
        return self._comparisonOperatorHelper(operator.add, other)

    def __sub__(self, other):
        return self._comparisonOperatorHelper(operator.sub, other)

    def __iadd__(self, other):
        self._balance = self + other
        return self
    def __isub__(self, other):
        self._balance = self - other
        return self

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
