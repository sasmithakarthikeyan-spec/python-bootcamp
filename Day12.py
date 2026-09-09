#task 1
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    @property
    def salary(self):
        return self.__salary

emp1=Employee("Arun",50000)

print(emp1.name)
print(emp1.salary)'''

#task2
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("Invalid salary")

emp1=Employee("Arun",50000)
print(emp1.salary)
emp1.salary=60000
print(emp1.salary)
emp1.salary=-5000'''

#mini project
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

account1=BankAccount("Arun",50000)


while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Balance:", account1.balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(amount)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")