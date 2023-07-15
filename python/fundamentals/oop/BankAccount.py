class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * (self.int_rate / 100)
            self.balance += interest
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# Create two accounts
account1 = BankAccount(5, 1000)
account2 = BankAccount(3, 500)

# Perform operations on account1
account1.deposit(500).deposit(1000).deposit(200).withdraw(700).yield_interest().display_account_info()

# Perform operations on account2
account2.deposit(300).deposit(200).withdraw(100).withdraw(50).withdraw(200).withdraw(100).yield_interest().display_account_info()

# Print all account information
BankAccount.print_all_accounts()