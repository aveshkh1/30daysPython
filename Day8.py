# 🚀 Day 8: More Questions on Python Functions

# Q1: WAF to find the maximum of 3 numbers
def max_nums(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

print(f"{max_nums(1, 4, 5)} is the greatest")

# Q2: WAF that returns the sum of all numbers from 1 to n
def sum_of_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(f"Sum of numbers from 1 to 5 is {sum_of_n(5)}")

# Q3: WAF to count the number of vowels in a string
def vowel_count():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    return count

print(f"Number of vowels in the string is {vowel_count()}")

# Q4: WAF to reverse a given string
def reverse_str(s):
    return s[::-1]

print(f"Reversed string: {reverse_str('Tanuja')}")

# Q5: WAF that returns True if the given string is a palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(f"Is 'AVesh' a palindrome? {is_palindrome('AVesh')}")

# Q6: WAF to generate a Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

print("Fibonacci series up to 4 terms:")
fibonacci(4)
