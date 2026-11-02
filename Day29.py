from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=15)
    course: str | None=None
    age: int = Field(ge=16, le=20)

'''student1 = Student(
    id=1,
    name="Sash",
    course="Python"
)

print(student1)
print(student1.name)
print(student1.course)

#data validation

student2 = Student(
    id=2,
    name="Ramesh",
    course="SQL"
)

print(student2)

#missing value
student3 = Student(
    id=3,
    name="Kanya"
)

print(student3)

student4 = Student(
    id=4,
    name="Sasmithakarthikeyan",
    course="Python"
)

print(student4)

student6 = Student(
    id=6,
    name="Kanya",
    course="Python",
    age=20
)

print(student6)'''

class User(BaseModel):
    name: str
    email: EmailStr

user1 = User(
    name="Sash",
    email="sash@gmail.com"
)

print(user1)

user1 = User(
    name="Sash",
    email="sash123"
)

print(user1)

