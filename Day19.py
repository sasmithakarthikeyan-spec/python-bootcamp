#task 1
'''from dataclasses import dataclass

@dataclass
class Employee:
    name:str
    salary:float
    department:str

emp=Employee("Ramesh",35000.0,"Sales")
print(emp.name)
print(emp.salary)
print(emp.department)'''

#task 2
'''from enum import Enum

class Status(Enum):
    PENDING="Pending"
    COMPLETED="Completed"
    CANCELLED="Cancelled"

print(Status.PENDING)
print(Status.COMPLETED.value)'''

#mini project
from enum import Enum

class Department(Enum):
    IT = "IT"
    HR = "HR"
    SALES = "Sales"
    FINANCE = "Finance"


class Status(Enum):
    ACTIVE = "Active"
    ON_LEAVE = "On Leave"
    RESIGNED = "Resigned"

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float
    department: Department
    status: Status

emp1 = Employee(
    "Ramesh",
    35000.0,
    Department.SALES,
    Status.ACTIVE
)

emp2 = Employee(
    "Priya",
    45000.0,
    Department.IT,
    Status.ON_LEAVE
)
print(emp1)
print(emp2)

def display_employee(employee: Employee) -> None:
    print("========================")
    print("EMPLOYEE DETAILS")
    print("========================")
    print(f"Name: {employee.name}")
    print(f"Salary: {employee.salary}")
    print(f"Department: {employee.department.value}")
    print(f"Status: {employee.status.value}")

display_employee(emp1)
display_employee(emp2)