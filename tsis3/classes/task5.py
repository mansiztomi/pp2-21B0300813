class BAcc():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount Balance: ${self.balance}'
    def deposit(self, dp_amount):
        self.balance += dp_amount
        print("Deposit accepted")
    def withdraw(self, wt_amount):
        if self.balance >= wt_amount:
            self.balance -= wt_amount
            print("Withdrawal accepted")
        else:
            print("Unavailable bank account")
acc1 = BAcc('Tomi', 500)
print(acc1)
acc1.deposit(500)
acc1. withdraw(200)
acc1.withdraw(1000)