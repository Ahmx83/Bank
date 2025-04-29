import json

def main():
    print("Welcome to Sudora Bank")


class Account:
    """Creates a new account"""
    def __init__(self, name: str, account_no: int, pin: int, balance: float):
        self.name = name.capitalize()
        self.account_no = account_no
        self.pin = pin
        self.balance = balance

        with open("ledgers.json", "r") as fp:
            customers = json.load(fp)
        with open("ledgers.json", "w") as fp:
            customers[self.name] = self.__dict__
            json.dump(customers, fp, indent=2)

def getValidInput(input_, invalid_msg, *expected):
    inp = input("> ")
    while inp not in expected:
        print(invalid_msg)
        inp = input("> ")
    return input_


def CheckBalance(account:Account):
    with open("ledgers.json", "r") as fp:
        customers = json.load(fp)
    return customers[account.name]["balance"]



aa = Account("ahmed", 1222, 4444, 5555)
print(CheckBalance(aa))