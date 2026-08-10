#mini project-2

print("==============")
print("STUDENT REPORT")
print("==============")
students={
    "Sash":85,
    "Anu":92,
    "Ravi":67,
    "Priya":95,
    "Kavin":35
}
print(students)

top_students={
    name:mark 
    for name,mark in students.items()
    if mark>=80
}
print("\nTop Students:")
print(top_students)

passed_students={
    name:mark
    for name,mark in students.items()
    if mark>=40
}
print("\nPassed Students:")
print(passed_students)

failed_students={
    name:mark
    for name,mark in students.items()
    if mark<=40
}
print("\nFailed Students:")
print(failed_students)

grades={
    name:"A" if mark>=90 else
         "B" if mark>=75 else
         "C" if mark>=60 else
         "D" if mark>=40 else
         "F"
    for name,mark in students.items()
}
print("\nStudent Grades:")
print(grades)