class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print('Balance: ' + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self
        
    @classmethod
    def print_all_accounts(cls):
        account_number = 1
        for account in cls.all_accounts:
            print(f'Account number {account_number}: Balance - ${account.balance}, Interest Rate - {account.int_rate * 100}%')
            account_number = account_number + 1


my_bank_account = BankAccount(0.02, 250.00)
my_bank_account.deposit(50.00).deposit(75.00).deposit(100.00).withdraw(300.00).yield_interest().display_account_info()

your_bank_account = BankAccount(0.01, 100.00)
your_bank_account.deposit(150).deposit(125).withdraw(50).withdraw(100).withdraw(100).withdraw(30).yield_interest().display_account_info()

BankAccount.print_all_accounts()