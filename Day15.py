#task 1
'''def add_message(func):

    def python():
        print("Welcome tp python!")

        func()

    return python

@add_message
def welcome():
    print("have a great day")

welcome()'''

#task 2
'''def add_message(func):
    def python(*args):
        print("Starting function")

        func(*args)

        print("Function completed!")

    return python

@add_message
def student(name,course):
    print("Student:",name)
    print("Course:",course)

student("Sash","Python")'''

#task 3
'''def add_message(func):
    def python(**kwargs):
        print("Starting function")

        func(**kwargs) 

        print("Function completed!")
    return python

@add_message
def student(name,course):
    print("Student:",name)
    print("Course:",course)

student(name="Sash",course="Python")'''

#task 4
'''def login_message(func):
    def welcome(**kwargs):
        print("Login successful")

        func(**kwargs)

        print("Welcome to dashboard!")

    return welcome

@login_message
def user(name):
    print("Hello",name)

user(name="Sash")'''

#task 5
'''def calculate_time(func):
    def wrapper(*args,**kwargs):
        print("Calculation started")

        func(*args,**kwargs)

        print("Calculation completed")

    return wrapper

@calculate_time
def add(a,b):
    print("Result:",a+b)

add(24,78)'''

#task 6
def logger(func):
    def wrapper(*args,**kwargs):
        print("Function started:", func.__name__)

        result=func(*args,**kwargs)

        print("Function completed:",func.__name__)

        return result
    return wrapper

@logger
def multiply(a,b):
    return a*b

result=multiply(23,5)
print("Result:",result)