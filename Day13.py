#task 1
'''from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self,radius):
        pass

class Circle(Shape):
    def area(self,radius):
        print(f"The area is {3.14*radius**2}")

circle=Circle()

circle.area(50)'''

#task 2
'''from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self,length,breadth):
        pass

class Rectangle(Shape):
    def area(self,length,breadth):
        print(f"The area is {length*breadth}")

rect=Rectangle()

rect.area(42,18)'''

#miniproject
from abc import ABC,abstractmethod
class Payment(ABC):
    def pay(self,amount):
        pass

class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} using UPI")

class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} using Card")

upi=UPIPayment()
card=CardPayment()

upi.pay(3000)
card.pay(4500)

