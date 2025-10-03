class BankAccount:
    def __init__(self, account_Balance=0):
        self.account_balance = account_Balance


    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        #return self.account_balance
        #print(self.account_balance)


    def withdraw(self, amount):
        if amount > 0:
            if amount < self.account_balance:
                self.account_balance -= amount
                

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
    

