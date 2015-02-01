#banking.py

class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            return self.balance
    
    def transfer(self, amount, account):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            account.balance = account.balance + amount
            

    #alternative transfer method        
        
    # def transfer(self, amount, account):
    #     if self.balance - amount >= 0:
    #         self.withdraw(amount)
    #         account.deposit(amount)       



# if __name__ == '__main__':
#     main()
