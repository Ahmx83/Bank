from bank import Account, Operations, ExistingAccount
from funcs import getValidInput


def main():
    print("Welcome to Sudura bank.\n"
          "Do you have an active account? (y/n)")
    y_n = getValidInput("Enter (y) if you have an existing account, "
                       "(n) if you don't.",
                       "y", "n", key = str.lower)
    print(y_n)
    if y_n == "y":
        # If customer has an existing account
        acc_no = None
        pin = None
        account = ExistingAccount(acc_no, pin)
        pass
    elif y_n == "n":
        # If customer needs a new account
        pass

if __name__ == '__main__':
    main()