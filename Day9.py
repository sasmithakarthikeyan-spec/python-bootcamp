#task 1
class Employee:

    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

    def __str__(self):
        return f"{self.name}-{self.salary}-{self.department}"

    def __len__(self):
        return len(self.name)

emp1= Employee("Darshan",50000,"Automobile")
emp2= Employee("Prem",45000,"Engineer")
print(len(emp1))