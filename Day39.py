#example 1
'''import asyncio

async def greet():
    print("Hello!")
    await asyncio.sleep(2)
    print("Welcome to Async Python!")

asyncio.run(greet())'''

#example 2
'''import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def task3():
    print("Task 3 started")
    await asyncio.sleep(1)
    print("Task 3 completed")

async def main():
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

asyncio.run(main())'''

#example 3
'''import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await task1()
    await task2()

asyncio.run(main())'''

#example 4
'''import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    t1=asyncio.create_task(task1())
    t2=asyncio.create_task(task2())

    print("Both tasks are scheduled")

    await t1
    await t2

asyncio.run(main())'''

#example 5
'''import asyncio

async def fetch_user():
    print("Fetching user details..")
    await asyncio.sleep(2)
    print("User details received!")

async def fetch_products():
    print("Fetching orders..")
    await asyncio.sleep(3)
    print("Products received!")

async def fetch_orders():
    print("Fetching orders..")
    await asyncio.sleep(1)
    print("Orders received!")

async def main():
    await asyncio.gather(
        fetch_user(),
        fetch_products(),
        fetch_orders()
    )

asyncio.run(main())'''

#example 5 - fastAPI
'''from fastapi import FastAPI
import asyncio

app=FastAPI()

@app.get("/")
async def home():
    return {
        "message":"Welcome to API Function"
    }

@app.get("/users")
async def get_users():
    await asyncio.sleep(2)

    return {
        "users":["Sash","Ramesh","Kanya"],
        "message":"users fetched successfully!"
    }'''

#example 6- fastAPI
'''from fastapi import FastAPI
import asyncio

app= FastAPI()

@app.get("/")
def home():
    return{
        "message":"Normal FastAPI function"
    }

@app.get("/async")
async def async_home():
    await asyncio.sleep(2)

    return {
        "message":"Asynchronous FastAPI function"
    }'''

#example 7
from fastapi import FastAPI
import asyncio

app=FastAPI()

async def task1():
    await asyncio.sleep(2)
    return "User details fetched!"

async def task2():
    await asyncio.sleep(3)
    return "Products fetched!"

async def task3():
    await asyncio.sleep(1)
    return "Orders fetched!"

@app.get("/")
async def home():
    return {
        "message":"Welcome to Async task Manager!"
    }

@app.get("/run-tasks")
async def run_tasks():
    results= await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

    return {
        "results":results,
        "message":"All tasks completed successfully"
    }