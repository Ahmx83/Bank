from bank import Account, Operations

def main():
    print("""Welcome to Sudura bank.
    Do you have an active account? (y/n)""")
    yn = getValidInput("Enter (y) if you have an existing account, "
                       "(n) if you don't.",
                       "y", "n")



def getValidInput(invalid_msg, *expected):
    """Keeps asking for input until given an expected input.
     Lowercases the input if it's a string."""
    ip = input("> ")
    if type(ip) == str:
        ip.lower()
    while ip not in expected:
        print(invalid_msg)
        inp = input("> ")
    return ip


if __name__ == '__main__':
    main()