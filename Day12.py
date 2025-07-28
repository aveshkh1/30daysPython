#Day12:Deep dive into the main pillars of the OOPS
#Abstraction
#Encapsulation
#Inheritance
#Polymorphism

#Abstraction
#Hiding the implemention details of the class showing only the necesary features to the end user

#Encapsulation
#wrapping the data and functions into single unit(object)
#EX
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.cluctch=False
    def start(self):
        self.cluctch=True
        self.acc=True
        print("Car Started")

car1=Car()
car1.start()