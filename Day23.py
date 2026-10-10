'''import sqlite3

connection = sqlite3.connect("day23.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

connection.commit()

print("Database connected!")
print("Products table created!")

#add record
def add_product(name, price, quantity):
    cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """, (name, price, quantity))

    connection.commit()

    print(f"{name} added successfully!")


add_product("Keyboard", 1200.00, 10)
add_product("Mouse", 500.00, 20)
add_product("Monitor", 8500.00, 5)

#display record

def display_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("========================")
    print("ALL PRODUCTS")
    print("========================")

    for product in products:
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Price: {product[2]}")
        print(f"Quantity: {product[3]}")
        print("------------------------")


display_products()

#update record

def update_product(product_id, new_price):
    cursor.execute("""
    UPDATE products
    SET price = ?
    WHERE id = ?
    """, (new_price, product_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("Product not found!")
    else:
        print("Product updated successfully!")


update_product(1, 1500.00)

display_products()

#delete record

def delete_product(product_id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        print("Product not found!")
    else:
        print("Product deleted successfully!")


delete_product(3)

display_products()'''

#mini project- Product Management System
import sqlite3

connection=sqlite3.connect("day23.db")
cursor=connection.cursor()

#CREATE TABLE
cursor.execute(""" CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price REAL NOT NULL,
quantity INTEGER NOT NULL)""")
connection.commit()

#INSERT DATA
def add_product(name,price,quantity):
    cursor.execute("""
    INSERT INTO products (name,price,quantity)
    VALUES (?,?,?)
    """,(name,price,quantity))

    connection.commit()
    print("Product added successfully")

#READ
def display_products():
    cursor.execute("SELECT * FROM products")
    products=cursor.fetchall()

    if not products:
        print ("NO PRODUCTS FOUND")
        return

    print("\n=======ALL PRODUCTS=======")
    for product in products:
        print(f"ID:{product[0]}")
        print(f"Name:{product[1]}")
        print(f"Price:{product[2]}")
        print(f"Quantity:{product[3]}")
        print("---------------------------")

#UPDATE
def update_product(product_id,new_price):
    cursor.execute("""
    UPDATE products
    SET price=?
    WHERE id=?
    """,(new_price,product_id))

    connection.commit()

    if cursor.rowcount==0:
        print("Product not found!")
    else:
        print("Product updated successfully!")

#DELETE
def delete_product(product_id):
    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (product_id,)
    )
    connection.commit()

    if cursor.rowcount==0:
        print("product not found")
    else:
        print("Product deleted successfully")

#MENU
while True:
    print("\n=====PRODUCT MANAGEMENT=====")
    print("1.Add Product")
    print("2.Display Products")
    print("3.Update Product Price")
    print("4.Delete Product")
    print("5.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        name=input("Enter product name:")
        price=float(input("Enter product price:"))
        quantity=int(input("Enter Quantity:"))

        add_product(name,price,quantity)

    elif choice=="2":
        display_products()

    elif choice=="3":
        product_id=int(input("Enter product ID:"))
        new_price=float(input("Enter new price:"))
        update_product(product_id,new_price)

    elif choice=="4":
        product_id=int(input("Enter product ID:"))

        delete_product(product_id)

    elif choice=="5":
        print("Exiting Product Management System!")
        break

    else:
        print("Invalid choice! Try again.")

connection.close()
print("Database connection closed and the records have been updated!")