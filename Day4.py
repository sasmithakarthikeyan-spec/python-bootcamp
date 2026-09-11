#mini project-4
class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")

    def check_balance (self):
        print(f"Current Balance:{self.balance}") 



print("===================")
print("BANK ACCOUNT DETAILS")
print("====================")

Name=input("Enter the account holder name-")
Balance=int(input("Enter the account balance-"))
account1=BankAccount(Name,Balance)

print("\nPRESS 1 to add deposit cash into your account")
print("PRESS 2 to withdraw amount from your account")
print("PRESS 3 to check your account balance")

check= int(input("\nEnter a option to process:"))

if check==1:
    amnt=int(input("Enter the amount to be deposited:"))
    account1.deposit(amnt)

elif check==2:
    amnt=int(input("Enter the amount to be withdrawn:"))
    account1.withdraw(amnt)

elif check==3:
    account1.check_balance()

else:
    print("Enter a valid option")

