#Day 11:Practicing more topics on OOPS
#@Staticmethod

class Student:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def print():
        print("Hello")

s1=Student("Avesh")
print(s1.name)
s1.print()

#Q2:Create student class that tables name and marks of 3 subjects as argument in constructor
#create a method to print the average

class Std:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def avg(self):
        print("The avg of the marks",(self.sub1+self.sub2+self.sub3)/3)
std1=Std("Gundu",35,45,66)
print(std1.name)
std1.avg()

#Another method to do this
class Student1:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg_score(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("Hello",self.name,"your avg score is",sum/3)
st2=Student1("AVesh",[75,85,88])
st2.avg_score()
