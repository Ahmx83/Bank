from bank import Account, Operations

dima = Account("dima", 9999, 9876, 7500)

x = Operations(dima)
bal = x.CheckBalance()
print(bal)