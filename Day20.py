# Day 20: Cognizant Interview Questions

# Q1: Program to take any number as input, then using a while loop
# divide it into individual digits and calculate the sum of digits.
number = int(input("Enter a number: "))
digit_sum = 0
temp = number

while temp > 0:
    n = temp % 10
    print(n, end=" ")
    digit_sum += n
    temp //= 10

print("\nSum of digits:", digit_sum)


# Q2: Find all Armstrong numbers within a specified range
start = int(input("\nEnter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Armstrong numbers between {start} and {end}: ", end="")
for number in range(start, end + 1):
    temp = number
    no_of_digits = len(str(number))
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** no_of_digits
        temp //= 10
    if armstrong_sum == number:
        print(number, end=" ")


# Q3: Display all prime numbers in the range 1 to 100
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nPrime numbers from 1 to 100: ", end="")
for i in range(1, 101):
    if is_prime(i):
        print(i, end=" ")
