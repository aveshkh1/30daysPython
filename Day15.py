#Day15:OOPs Concepts
class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    @property
    def percentage(self):
        return str((self.chem+self.phy+self.maths)//3)+'%'


s1=Student(45,55,77)
s1.phy=77
print(s1.percentage)

#Polymorphism:Operator overloading
#When the same operator is allowed to have different meaning according to the context
#operator and dunder functions
#a+b a.__add__(b)
#a-b a.__sub__(b)
#a*b a.__mul___(b)

