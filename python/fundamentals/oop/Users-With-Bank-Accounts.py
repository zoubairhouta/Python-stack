class BankAccount:
    accounts=[]
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully")
        else:
            print("Insufficient funds!")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance *= 1 + self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(f"Balance: ${account.balance}, Interest Rate: {account.int_rate * 100}%")


samir_account = BankAccount(0.02, 1000)
samira_account = BankAccount(0.03, 500)
samir_account.deposit(200).deposit(2000).deposit(5000).withdraw(
    400
).yield_interest().display_account_info()
samira_account.deposit(2050).deposit(20500).withdraw(4200).withdraw(4100).withdraw(
    4200
).withdraw(4200).display_account_info()
BankAccount.print_all_accounts()

