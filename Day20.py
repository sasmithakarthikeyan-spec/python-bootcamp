#task 1- counter
'''from collections import Counter

marks = [90, 80, 90, 75, 80, 90, 95]

count = Counter(marks)

print(count)
print(count[90])
print(count.most_common(2))'''

#task 2- defaultdict
'''from collections import defaultdict

subjects = defaultdict(list)

subjects["Sasmitha"].append("Python")
subjects["Sasmitha"].append("SQL")
subjects["Ramesh"].append("Java")
subjects["Ramesh"].append("C++")

print(subjects)
print(subjects["Sasmitha"])
print(subjects["Kanya"])'''

#task3
'''from collections import defaultdict

marks = defaultdict(int)

marks["Sasmitha"] += 10
marks["Sasmitha"] += 20
marks["Ramesh"] += 30

print(marks)
print(marks["Kanya"])'''

#task4- deque
'''from collections import deque

students = deque(["Sasmitha", "Ramesh", "Kanya"])

students.append("Priya")
students.appendleft("Arun")

print(students)

students.pop()
students.popleft()

print(students)'''

#task5- namedtuple
'''from collections import namedtuple

Employee=namedtuple("Employee",["name","salary","department"])

emp=Employee("Suresh",350000,"Sales")

print(emp.name)
print(emp.salary)
print(emp.department)'''

#mini. project

from collections import namedtuple, Counter, defaultdict, deque

Student = namedtuple("Student", ["name", "mark", "subject"])

student1 = Student("Sasmitha", 90, "Python")
student2 = Student("Ramesh", 80, "Python")
student3 = Student("Kanya", 90, "Python")

print(student1)
print(student1.name)
print(student1.mark)

student1 = Student("Sasmitha", 90, "Python")
student2 = Student("Ramesh", 80, "Python")
student3 = Student("Kanya", 90, "Python")

marks = [student1.mark, student2.mark, student3.mark]

mark_count = Counter(marks)

print(mark_count)

subjects = defaultdict(list)

subjects["Sasmitha"].append("Python")
subjects["Sasmitha"].append("SQL")

subjects["Ramesh"].append("Python")

subjects["Kanya"].append("Java")

print(subjects)
print(subjects["Sasmitha"])

student_queue = deque(["Sasmitha", "Ramesh", "Kanya"])

student_queue.append("Priya")
student_queue.appendleft("Arun")

print(student_queue)

student_queue.popleft()

print(student_queue)


