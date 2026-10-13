'''status_code = 404

if status_code == 200:
    print("Request successful!")
elif status_code == 404:
    print("Resource not found!")
elif status_code == 500:
    print("Server error!")
else:
    print("Something else happened!")'''

#task1

'''import json

product = """{
    "id": 1,
    "name": "Keyboard",
    "price": 1500,
    "quantity": 10
}
"""

json_data = json.dumps(product, indent=4)

print(json_data)
print(type(json_data))'''

#task 2
'''import json

json_data="""
{
"id":1,
"name":"Keyboard",
"price":1500,
"quantity":10
}
"""

product= json.loads(json_data)

print(product)
print(type(product))
print(product["name"])
print(product["price"])'''

#task 3

import json

product = {
    "id": 1,
    "name": "Keyboard",
    "price": 1500,
    "quantity": 10
}

with open("product.json", "w") as file:
    json.dump(product, file, indent=4)

print("Product saved successfully!")

#task4

with open("product.json", "r") as file:
    saved_product = json.load(file)

print("Product loaded successfully!")
print(saved_product)
print(type(saved_product))
print("Product name:", saved_product["name"])

#task 5

import json

products = [
    {"id": 1, "name": "Keyboard", "price": 1500},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Monitor", "price": 8500}
]

# Save products to a JSON file
with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

# Read products from the JSON file
with open("products.json", "r") as file:
    saved_products = json.load(file)

# Display each product
for product in saved_products:
    print("Product:", product["name"])
    print("Price:", product["price"])
    print("--------------------")


