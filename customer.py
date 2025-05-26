from typing import Literal
from account import Account


class ID:
    def __init__(self, name, age, gender: Literal["M", "F"]):
        self.name = name
        self.age = age
        self.gender = gender

class Customer:
    def __init__(self, id_: ID, account: Account):
        self.account = account

