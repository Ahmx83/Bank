from bank import Account, Operations, NewAccount, generateAccountNumber

dima = Account("dima", 69994, 9876, 7500)

op = Operations(dima)
bal = op.checkBalance()
print(bal)
take = op.withdraw(100)
give = op.deposit(99)

generateAccountNumber()