#mini project-3
print("=====================")
print("EMPLOYEE SALARY DATA")
print("=====================")

names=["Sash", "Anu", "Ravi",  "Priya"]
salaries=[45000, 60000, 35000, 75000]

employees=list(zip(names,salaries))
print("\nEmployees:")
print(employees)

updated_employees=list(map(lambda employees: (employees[0],employees[1]*1.10),employees))
print("\nUpdated Employees:")
print(updated_employees)

filter_employees=list(filter(lambda employees: (employees[1]>=60000),updated_employees))
print("\nFiltered Employees:")
print(filter_employees)

sorted_employees=sorted(updated_employees,key=lambda employee: employee[1],reverse=True)
print("\nSorted Employees:")
print(sorted_employees)

print("\nFinal Employee Ranking:")
for number,employees in enumerate(sorted_employees,start=1):
    print(f'{number}.{employees[0]}-{round(employees[1])}')