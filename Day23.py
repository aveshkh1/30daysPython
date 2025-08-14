# Day23: Interview Style Questions

# Q1: Write a program to determine whether a given number can be expressed as the sum of two prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    found = False
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(f"{n} = {i} + {n - i}")
            found = True
    if not found:
        print(f"{n} can't be expressed as sum of two prime numbers")

N = int(input("Enter the number: "))
sum_of_primes(N)

print("\n" + "-" * 40 + "\n")

# Q2: Write a program to check whether a given character is an alphabet or not.

# Using ASCII method
char = input("Enter the character: ")

if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
    print(f"{char} is an alphabet (Checked using ASCII method)")
else:
    print(f"{char} is not an alphabet (Checked using ASCII method)")

# Using built-in isalpha() method
if char.isalpha():
    print(f"{char} is an alphabet (Checked using isalpha method)")
else:
    print(f"{char} is not an alphabet (Checked using isalpha method)")

print("\n" + "-" * 40 + "\n")

# Q3: Write a program to determine the number of days in a given month of a specific year
# Taking into account leap years where February has 29 days and non-leap years where February has 28 days.

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def number_of_days(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return "Invalid month"

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
print(f"Number of days: {number_of_days(month, year)}")
