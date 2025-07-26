# Day10: Introduction to OOPS
# To map real-world scenarios, OOPS (Object-Oriented Programming) is introduced.

# Q1: Creating the basic class
class Student:
    name = 'Avesh'
    location = 'Bangalore'

s1 = Student()
print(s1.name)
print(s1.location)

# What is a Constructor?
# Constructor is a special method (__init__) which is automatically called when an object is created.

# Q2: Creating the Employee class and initializing the constructor
class Employee:
    def __init__(self, name, company, designation):
        self.name = name
        self.company = company
        self.designation = designation

e1 = Employee("Avesh", "Cognizant", "Data Scientist")
print(e1.name)
print(e1.designation)
print(e1.company)

# Q3: Methods in OOPS including instance method and static method
class Student1:
    def __init__(self, name):
        self.name = name

    def greet(self):  # Changed method name from print to greet
        print("Hello", self.name)

    @staticmethod
    def info():
        print("This is a Student class.")

st1 = Student1("Janu")
st1.greet()
Student1.info()  # Static method is called using the class name
