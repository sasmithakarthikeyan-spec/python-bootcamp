from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database
engine = create_engine("sqlite:///students.db")
print("Database created successfully!")

# Create model
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)

Base.metadata.create_all(engine)
print("Student table created successfully!")

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert student
student1 = Student(name="Sash", age=19, course="Python")

session.add(student1)
session.commit()
print("Student inserted successfully!")

# Update student
student = session.query(Student).filter_by(name="Sash").first()

if student:
    student.course = "SQL"
    session.commit()
    print("Student updated successfully!")

print("Update section executed!")

# Retrieve students
students = session.query(Student).all()

print("\nStudent Records:")

for student in students:
    print(student.id, student.name, student.age, student.course)

#delete record
student = session.query(Student).filter_by(id=33).first()

if student:
    session.delete(student)
    session.commit()
    print("Student deleted successfully!")

#retrieve record
students = session.query(Student).all()

print("\nUpdated Student Records:")

for student in students:
    print(student.id, student.name, student.age, student.course)

# Close session
session.close()


