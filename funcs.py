from typing import TypeVar

T = TypeVar('T')

def getValidInput(invalid_msg: str, *expected: T, key = None) -> T:
    """Keeps asking for input until given an expected input."""
    user_input = input("> ")
    if key:
        user_input = key(user_input)

    while user_input not in expected:
        print(invalid_msg)
        user_input = input("> ")
        if key:
            user_input = key(user_input)

    return user_input
