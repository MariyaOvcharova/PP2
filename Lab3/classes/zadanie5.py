class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance < money:
            print("Permission denied")
            print("Your balance", f"{self.balance}")
        else:
            self.balance -= money
            print("Your balance", f"{self.balance}")

cash = Account("Mariya", 1000000)
cash.deposit(450000)
cash.withdraw(20000)
