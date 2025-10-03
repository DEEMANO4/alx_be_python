class BankAccount:
    def __init__(self, account_Balance=0):
        self.account_balance = account_Balance


    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount


    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else : 
            return False
                
                

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
    

