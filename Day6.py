#program 1
'''try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")'''

#program 2
'''try:
    a = int(input("Enter a number: "))
    result = 100 / a
    print(result)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")'''

#program 3
'''try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
finally:
    print("Program finished")'''

#structure
'''try:
    # risky code
except ValueError:
    # handle error
else:
    # runs if no error
finally:
    # runs every time'''

#task 1
'''try:
    a=int(input("Enter a number:"))
except ValueError:
    print("Please enter a valid number")
else:
    print("Valid number")'''

#task 2
'''class InvalidAgeError(Exception):
    pass

age=int(input("Enter your age:"))
if age<18:
    raise InvalidAgeError("below 18 restricted")
else:
    print("Age is valid")
'''

#task 3
'''class InvalidAgeError(Exception):
    pass
try:
    age=int(input("enter your age:"))

    if age<18:
            raise InvalidAgeError("Below 18 restricted")
    print("Valid age")
except InvalidAgeError as e:
    print(e)'''

#task 4
import logging

logging.basicConfig(level=logging.INFO) 

logging.info("Program Started")
logging.warning("Wrong PIN")
logging.error("Transaction failed")

#mini project-6

class InsufficientBalanceError(Exception):
    pass

balance=5000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount=int(input("Enter the amount to be deposited"))
        balance=balance+amount
        print("New Balance:",balance)

    elif choice == "3":
        print("Withdraw")

    elif choice == "4":
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")