#task 1 type hinting
'''name:str="Sasmitha"
age:int=19
height:float=159.50
is_student:bool=True'''

#task 2
'''def student_info(name:str,age:int,mark:float):
    return f"Name:{name},Age:{age},Mark:{mark}"
print(student_info("Suruthi",20,87.5))'''

#task 3
'''from typing import Optional

def get_name(name: Optional[str]) -> str:
    if name is None:
        return "No name provided"
    return name

print(get_name("Sasmitha"))
print(get_name(None))'''

#task 4
'''from typing import Union

def display_id(student_id: Union[int, str]) -> str:
    return f"Student ID: {student_id}"

print(display_id(101))
print(display_id("ST101"))'''

#task5
'''from typing import Optional

def student_details(name:str,age:int,phone:Optional[str]):
    if phone is None:
        return f"Name:{name},Age:{age},Phone:Not provided"
    return f"Name:{name},Age:{age},Phone:{phone}"

print(student_details("Vishal",20,"814805742h"))
print(student_details("sas",24,None))'''

#task 6
'''from typing import Union

def show_price(price:Union[int,float]):
    return f"Price:{price}"
print(show_price(500))
print(show_price(499.50))'''

#task 7
from typing import Any

def display_data(data:Any):
    return f"Data:{data}"

print(display_data(100))
print(display_data("Python"))
print(display_data([1,2,3]))
