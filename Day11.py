#task 1
'''class Bike:
    def move(self):
        print("Bike is moving")

class Car:
    def move(self):
        print("Car is driving")

bike=Bike()
car=Car()

bike.move()
car.move()'''

#task2
'''class Bike:
    def move(self):
        print("Bike is moving")

class Car:
    def move(self):
        print("Car is driving")

def start_moving(vehicle):
    vehicle.move()

bike=Bike()
car=Car()

start_moving(bike)
start_moving(car)'''

#task3
'''class Bike:
    def move(self):
        print("Bike is moving")

class Car:
    def move(self):
        print("Car is driving")

class Robot:
    def move(self):
        print("Robot is moving")

def start_moving(vehicle):
    vehicle.move()

bike=Bike()
car=Car()
robot=Robot()

start_moving(bike)
start_moving(car)
start_moving(robot)'''

#miniproject
class UPIPayment:
    def pay(self,amount):
        print(f"Paid ${amount} using UPI")

class CardPayment:
    def pay(self,amount):
        print(f"Paid ${amount} using Card")

class CashPayment:
    def pay(self,amount):
        print(f"Paid ${amount} using Cash")

def make_payment(payment_method,amount):
    payment_method.pay(amount)

upi=UPIPayment()
card=CardPayment()
cash=CashPayment()

make_payment(upi, 3000)
make_payment(card, 5000)
make_payment(cash, 2000)