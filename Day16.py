#task 1
'''def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for num in count_numbers():
    print(num)'''

#task 2
'''def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def count_number():
    for i in range(1,6):
        yield i

for num in count_number():
    print(num)
'''

#task 3
'''def count_number():
    for i in range(2,11,2):
        yield i

for num in count_number():
    print(num)'''

#task 4
'''def fruits():
    yield "Apple"
    yield "Mango"
    yield "Strawberry"
    yield "Banana"

fruits=fruits()

print(next(fruits))
print(next(fruits))
print(next(fruits))
print(next(fruits))'''

#task 5
'''def squares(n):
    for i in range(1,n+1):
        yield i*i

for value in squares(5):
        print(value)'''

#task6
'''squares=(x*10 for x in range(1,6))
for values in squares:
    print(values)'''

#mini project
print("==========================")
print("NUMBER GENERATOR")
print("==========================")

def number_generator(start, end):
    for i in range(start, end + 1):
        yield i


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("\nGenerated numbers:")

for number in number_generator(start, end):
    print(number)