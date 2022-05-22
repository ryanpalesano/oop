class BankAccount:
    # new class attritubte, a list of all the accounts!!
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # class method to change the name of the bank

    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self


    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

savings = BankAccount(.02, 1000)
checking = BankAccount(.1, 50000)

savings.deposit(10).deposit(100).deposit(80).withdraw(50).yield_interest().display_account_info()
checking.deposit(1000).deposit(250).deposit(100).withdraw(475).yield_interest().display_account_info()

BankAccount.print_all_accounts()