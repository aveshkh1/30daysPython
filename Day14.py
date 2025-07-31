# Day14: Studying main pillars of OOPS in Python

# -------------------------------
# Example 1: del keyword
# -------------------------------
class Company:
    def __init__(self, employee, emp_id):
        self.employee_name = employee
        self.emp_id = emp_id

emp1 = Company("Manoj", 1)
print("Employee Name:", emp1.employee_name)
del emp1.employee_name

try:
    print(emp1.employee_name)
except AttributeError:
    print("employee_name has been deleted")

print("Employee ID:", emp1.emp_id)

del emp1
try:
    print(emp1)
except NameError:
    print("emp1 object has been deleted")

# -------------------------------
# Example 2: Private Attribute using __ (Encapsulation)
# -------------------------------
class Acc:
    def __init__(self, acc_number, acc_password):
        self.acc_number = acc_number
        self.__acc_password = acc_password  # private variable

    def reset_pass(self):
        print("Accessing private password:", self.__acc_password)

acc1 = Acc(1234, "Aveshkha1@")
print("Account Number:", acc1.acc_number)
acc1.reset_pass()

# -------------------------------
# Example 3: Static Methods
# -------------------------------
class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class CarName(Car):
    def __init__(self, name):
        self.name = name

car1 = CarName("Toyota")
print("Car Brand:", car1.name)
car1.start()
car1.stop()

# -------------------------------
# Example 4: Multilevel Inheritance
# -------------------------------
class Type(CarName):
    def __init__(self, name, car_type):
        super().__init__(name)
        self.car_type = car_type

type1 = Type("Tesla", "EV")
print("Car Name:", type1.name)
print("Car Type:", type1.car_type)
type1.start()

# -------------------------------
# Example 5: super() Method (Constructor Chaining)
# -------------------------------
class Company:
    def __init__(self, name):
        self.name = name

class Employees(Company):
    def __init__(self, company_name, employee_name):
        super().__init__(company_name)  # calling parent constructor
        self.employee_name = employee_name

e1 = Employees("Deloitte", "Avesh")
print("Company:", e1.name)
print("Employee:", e1.employee_name)
