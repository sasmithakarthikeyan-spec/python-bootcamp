#task 1
'''numbers=[10,20,30,40,50]

iterator=iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))'''

#task 2
'''class Numbers:
    def __init__(self):
        self.number = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.number<=50:
            value=self.number
            self.number+=10
            return value
        else:
            raise StopIteration

numbers=Numbers()

for num in numbers:
    print(num)'''

#task3- Context Manager
'''with open("sample.txt","w")as file:
    file.write("Python Context Manager")

print("File operation completed")'''

#task 4
'''with open("sample.txt","r")as file:
    content=file.read()

print(content)'''

#task 5
'''with open("sample.txt","a")as file:
    file.write("\nLearning Python!")

print("New content added")'''

#task6
'''class MyFile:
    def __enter__(self):
        print("File opened")
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        print("File closed")

with MyFile():
    print("Working with file")'''

#task 7- program stopped at zero division error but still prints the output
'''class MyContext:

    def __enter__(self):
        print("Starting")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Error:", exc_value)
        print("Finished")


with MyContext():
    print("Inside")
    10 / 0'''

#mini project
'''print("==================")
print("FILE MANAGER")
print("==================")

class FileManager:

    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        print("File opened")
        self.file=open(self.filename,self.mode) 
        return self.file

    def __exit__(self,exc_type,exc_vaalue,traceback):
        self.file.close()
        print("File closed")

with FileManager("data.txt","w")as file:   
    file.write("Learning Context Managers in Python!")

print("File operation completed!")'''

#task 8
'''class Connection:
    def __enter__(self):
        print("Connection opened")
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        print("Connection closed")

with Connection():
    print("Working with connection")'''

#task 9
class FileWriter:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_value,traceback):
        self.file.close()
        print("File Closed")

with FileWriter("notes.txt","w")as file:
    file.write("Python is fun")

print("File operation performed")

#task 10
with FileReader("notes.txt")as file:
    content=file.read()
    print(content)








