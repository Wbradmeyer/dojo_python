class BankAccount:
    all_accounts = []

    def __init__(self, name, int_rate, balance = 0):
        self.name = name
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

    def display_account_info(self, user_name):
        print(f'User: {user_name}, {self.name} Balance: ' + str(self.balance))
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



class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.checking_account = BankAccount('Checking', 0.02, 0)
        self.savings_account = BankAccount('Savings', 0.03, 0)

    def make_deposit(self, account, amount):
        if account == self.checking_account:
            self.checking_account.deposit(amount)
        else:
            self.savings_account.deposit(amount)
        return self

    def make_withdrawal(self, account, amount):
        if account == self.checking_account:
            self.checking_account.withdraw(amount)
        else:
            self.savings_account.withdraw(amount)
        return self

    def display_user_balance(self, account):
        if account == self.checking_account:
            self.checking_account.display_account_info(self.first_name)
        else:
            self.savings_account.display_account_info(self.first_name)
        return self
    
    def transfer_money(self, amount, other_user):
        self.make_withdrawal(self.checking_account, amount)
        other_user.checking_account.deposit(amount)
        return self


# BankAccount.print_all_accounts()

user_ben = User('Ben', 'Jerry')
user_ben.make_deposit(user_ben.checking_account, 500).make_withdrawal(user_ben.checking_account, 150).display_user_balance(user_ben.checking_account)
user_ben.make_deposit(user_ben.savings_account, 100).display_user_balance(user_ben.savings_account)

user_frannie = User('Frannie', 'McFarland')
user_ben.transfer_money(200, user_frannie).display_user_balance(user_ben.checking_account)
user_frannie.display_user_balance(user_frannie.checking_account)