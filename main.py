from bank import Account, Operations

def main():
    print("Welcome to Sudura bank.")


def getValidInput(input_, invalid_msg, *expected):
    """Keeps asking for input until given an expected input."""
    inp = input("> ")
    while inp not in expected:
        print(invalid_msg)
        inp = input("> ")
    return input_

if __name__ == '__main__':
    main()