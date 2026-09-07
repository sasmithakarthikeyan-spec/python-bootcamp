#task 1
'''class Vehicle():
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
car1=Car()
car1.start()
car1.drive()'''

#task 2
'''class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_name(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
    def display_team(self):
        print("Team Size:",self.team_size)

manager1 = Manager("Suresh", 35000, 6)

manager1.display_name()
manager1.display_team()'''

#task 3
class Battery:
    def charge(self):
        print("Battery is charging")

class Mobile:
    def __init__(self):
        self.battery=Battery()

    def use(self):
        self.battery.charge()
        print("Mobile is being used")

mobile1=Mobile()
mobile1.use()