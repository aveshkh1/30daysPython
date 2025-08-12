# Day 22: Interview Questions

# Q1: Create a program that adds two fractions entered by the user,
# where each fraction is defined by a Numerator and a Denominator,
# and the resulting sum is displayed in simplified form.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def add_fractions(num1, den1, num2, den2):
    numerator_sum = num1 * den2 + num2 * den1
    denominator_sum = den1 * den2

    common_divisor = gcd(numerator_sum, denominator_sum)
    numerator_sum //= common_divisor
    denominator_sum //= common_divisor
    return numerator_sum, denominator_sum

numerator1 = int(input("Enter the numerator1: "))
denominator1 = int(input("Enter the denominator1: "))
numerator2 = int(input("Enter the numerator2: "))
denominator2 = int(input("Enter the denominator2: "))

result_num, result_den = add_fractions(numerator1, denominator1, numerator2, denominator2)
print(f"The sum of fractions in simplified form is: {result_num}/{result_den}")

# Q2: Write a program to calculate the number of permutations
# in which N people can occupy R seats in a classroom.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def permutations(N, R):
    return factorial(N) // factorial(N - R)

N = int(input("Enter number of people (N): "))
R = int(input("Enter number of seats (R): "))
print(f"Number of permutations: {permutations(N, R)}")
