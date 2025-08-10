# Day 21 Basic Interview Questions

# Q1: Write a program to check if a number is a Harshad number
# Harshad number is a positive number that is divisible by the sum of its digits

number = int(input("Enter the number: "))
original_number = number
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

if original_number % sum_of_digits == 0:
    print(f"{original_number} is a Harshad number")
else:
    print(f"{original_number} is not a Harshad number")


# Q2: Write a program to find the factors of a given number
# Different methods for the task

# --- Basic method ---
number = int(input("\nEnter the number: "))
print(f"Factors of {number} are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print()

# --- Half range optimization method ---
number = int(input("\nEnter the number: "))
print(f"Factors of {number} are:")
for i in range(1, number // 2 + 1):
    if number % i == 0:
        print(i, end=" ")
print(number)
print()

# --- Square root method ---
num = int(input("\nEnter the number: "))
factors = set()
for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        factors.add(i)
        factors.add(num // i)
print(f"Factors of {num} are: {sorted(factors)}")
