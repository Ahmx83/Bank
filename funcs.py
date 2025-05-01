from typing import TypeVar

T = TypeVar('T')

def getValidInput(invalid_msg: str, *expected: T) -> T:
    """Keeps asking for input until given an expected input.
     Lowercases the input if it's a string."""
    ip = input("> ")
    if type(ip) == str:
        ip.lower()
    print(ip, expected)
    while ip not in expected:
        print(invalid_msg)
        ip = input("> ")
    return ip