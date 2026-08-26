import json
import logging

logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#checks and returns from json file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

expenses=load_expenses()

print("===============")
print("EXPENSE TRACKER")
print("===============")

#saves entry to the json file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")

def add_expense():
    date=input("Enter date:")
    ticket=input("Enter ticket:")
    category=input("Enter category:")
    description=input("Enter description:")
    location=input("Enter location:")
    try:
        amount=float(input("Enter amount:"))
    except ValueError:
        print("Please enter a valid amount")
        logging.warning("Invalid amount entered")
        return

    expense={
        "date":date,
        "ticket":ticket,
        "category":category,
        "description":description,
        "location":location,
        "amount":amount
    }

    expenses.append(expense)
    logging.info("Expense added successfully")
    save_expenses()

    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No data found")
        return
        
    for expense in expenses:
        print("=======================")
        print("Date:",expense["date"])
        print("Ticket:",expense["ticket"])
        print("Category:",expense["category"])
        print("Description:",expense["description"])
        print("Location:",expense["location"])
        print("Amount:",expense["amount"])

def total_expenses():
    if not expenses:
        print("No data found")
        return
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print("Total Expense:",total)

def search_expenses():
    category=input("Enter category to search:")
    found=False

    for expense in expenses:
        if expense["category"].lower()==category.lower():
            print("======================")
            print("Date:",expense["date"])
            print("Ticket:",expense["ticket"])
            print("Category:",expense["category"])
            print("Description:",expense["description"])
            print("Location:",expense["location"])
            print("Amount:",expense["amount"])

            found= True

    if not found:
        print("Noo expenses found for this category")



while True:
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Total Expense")
    print("4.Search Expense")
    print("5.Exit")
    try:
        check = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if check==1:
        add_expense()
    elif check==2:
        view_expenses()
    elif check==3:
        total_expenses()
    elif check==4:
        search_expenses()
    elif check==5:
        print("Exited!")
        break






     
    
            

            
            
            

            
            

             
