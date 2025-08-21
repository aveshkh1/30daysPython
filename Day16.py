# Day 16: OOPS Challenge
# Q1: Complex Number Class with Operator Overloading
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(3, 5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()


# Q2: Circle Class - Area and Perimeter
class Circle:
    def __init__(self, r):
        self.r = r

    def Area(self):
        print("The area is", (22/7) * self.r**2)

    def perimeter(self):
        print("The perimeter is", 2 * (22/7) * self.r)

c1 = Circle(21)
c1.Area()
c1.perimeter()


# Q3: Employee and Engineer Inheritance
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

e1 = Engineer("Avesh", 21, "Data Scientist", "IT", 55000)
e1.showDetails()


# Q4: Order Class using __gt__ (Greater Than) Dunder Method
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

o1 = Order("Chips", 50)
o2 = Order("Biscuit", 20)
print(o1 > o2)  # Output: True
