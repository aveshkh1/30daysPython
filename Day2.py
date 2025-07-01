# Day 2 – Conditional Statements and Input Function in Python
# Q1. Check if the number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It's an even number")
else:
    print("It's an odd number")
# Q2. Check whether a character is a Vowel or Consonant
ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("It's a vowel")
else:
    print("It's a consonant")
# Q3. Age Group Classifier
age = int(input("Enter the age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenage")
elif 20 <= age <= 60:
    print("Adult")
else:
    print("Senior Citizen")
# Q4. Find the Largest of 4 Numbers
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))
if a > b and a > c and a > d:
    print(f"{a} is the greatest")
elif b > c and b > d:
    print(f"{b} is the greatest")
elif c > d:
    print(f"{c} is the greatest")
else:
    print(f"{d} is the greatest")
