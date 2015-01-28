# Can you make this code work?

import banking
from sys import exit

my_checking_account = banking.BankAccount()
my_savings_account = banking.BankAccount()

# 1. Basic account functionality
my_checking_account.balance = 0.00
my_checking_account.deposit(100.00)
my_checking_account.deposit(200.00)
my_checking_account.deposit(300.00)
my_checking_account.deposit(600.00)
my_checking_account.withdraw(200.00)

if my_checking_account.balance != 1000.00:
    print("This bank can't be trusted! Failed on step 1.")
    exit()

# 2. Transfer between two accounts
my_savings_account.balance = 1000.00
my_savings_account.transfer(500.00, my_checking_account)

if my_checking_account.balance != 1500.00:
    print("This bank can't be trusted! Failed at step 2.")
    exit()

# 3. Guard against overdrafts
my_checking_account.withdraw(10000.00)
if my_checking_account.balance != 1500.00:
    print("This bank can't be trusted! Failed at step 3.")

# 4. Guard against overdraft during transfer
my_checking_account.transfer(10000.00, my_savings_account)
if my_checking_account.balance != 1500.00:
    print("This bank can't be trusted! Failed at step 4.")

# At this point the checking account should have $1500
# and the savings account should have $500
print("Here are the final balances:")
print("Checking account: ", my_checking_account.balance)
print("Savings account: ", my_savings_account.balance)



