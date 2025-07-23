# Day 7: Functions in Python

# Function: A block of code used to increase reusability.

# Q1: WAF (Write a Function) to add 2 numbers
def add(a, b):
    return a + b

# Example:
print("Sum:", add(5, 10))


# Q2: WAF to print even numbers from 1 to 100
def even_numbers():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")

print("\nEven numbers from 1 to 100:")
even_numbers()


# Q3: WAF to check if a number is prime
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example:
print("\nIs 3 prime?", prime(3))


# Q4: WAF to return the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example:
print("Factorial of 5 is:", factorial(5))
