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

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def create_account(self, account_name, int_rate, balance=0):
        account = BankAccount(int_rate, balance)
        self.accounts[account_name] = account
    
    def deposit(self, account_name, amount):
        if account_name in self.accounts:
            account = self.accounts[account_name]
            account.deposit(amount)
            print(f"${amount} deposited to {account_name} successfully")
        else:
            print("Account not found.")
    
    def withdraw(self, account_name, amount):
        if account_name in self.accounts:
            account = self.accounts[account_name]
            account.withdraw(amount)
        else:
            print("Account not found.")
    
    def display_account_info(self, account_name):
        if account_name in self.accounts:
            account = self.accounts[account_name]
            print(f"Account: {account_name}")
            account.display_account_info()
        else:
            print("Account not found.")
    
    def yield_interest(self, account_name):
        if account_name in self.accounts:
            account = self.accounts[account_name]
            account.yield_interest()
            print(f"Interest yielded for {account_name}")
        else:
            print("Account not found.")
    