class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance


    def deposit(self, amount):
        if amount > 0:
            self.account_balance = self.account_balance + amount
            print(self.account_balance)


    def withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
        

    def display_balance(self):
        print(self.account_balance)
    

