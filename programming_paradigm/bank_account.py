class BankAccount:
    def __init__(self, Current_Balance):
        self.account_balance = Current_Balance


    def deposit(self, amount):
        self.account_balance += amount
        #print(self.account_balance)


    def withdraw(self, amount):
        if amount > 0:
            if amount < self.account_balance:
                self.account_balance = self.account_balance - amount
                return self.account_balance
        

    def display_balance(self):
       ## return self.account_balance
        print("Current Balance:", self.account_balance)
    

