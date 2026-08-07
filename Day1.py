#prog1
'''def greet(name):
    return f"Hello,{name}!"
print(greet("Sash"))'''

#prog2
'''def square(num):
    return num*num
print(square(5))'''

#prog3
'''def wel(name):
    return f"Hello,{name}!"
print(wel("Guest"))'''

'''def wel(name):
    return f"Hello,{name}!"
print(wel("Sash"))'''

#challenge1
'''def calculate_total(*num):
    total=0
    for no in num:
        total+=no
    return total
    
print(calculate_total(10,20,30,40,50,60))'''

#challenge2
'''def student_details(**details):
    for key,value in details.items(): 
        print(key,":",value)
student_details(
    name="Sasmitha",
    age=19,
    college="Kongu Arts and Science College"
)'''   

#mini project-1
'''print("__________________________")
print("PYTHON CONSOLE CALCULATOR")
print("__________________________")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Exponent")

check=int(input("Enter your choice: "))

if(check==1):
    print(a+b)
elif(check==2):
    print(a-b)
elif(check==3):
    print(a*b)
elif(check==4):
    if(b!=0):
        print(a/b)
    else:
        print("Division by zero not possible")
elif(check==5):
    print(a%b)
elif(check==6):
    print(a**b)
else:
    print("Invalid choice. Please enter a number from 1 to 6")'''