# Day24: Interview level questions

# Q1: Write a program to find the longest palindrome in an array,
# where the goal is to identify and print the element
# with the longest length and palindrome characteristics.

def is_palindrome(s):
    s = str(s)
    s = s.lower()
    return s == s[::-1]

def longest_palindrome(arr):
    longest = ""
    for element in arr:
        if is_palindrome(element):
            if len(str(element)) > len(longest):
                longest = str(element)
    return longest if longest != "" else None

arr = ["Madam", 121, "Kayak", "deep", "deified", "noon"]
print("Longest Palindrome in the array is:", longest_palindrome(arr))


# Q2: Write a program to calculate the factorial of a large number,
# considering the multiplication of all positive integers up to the given number
# and handling cases such as 0, 1, and negative numbers

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter the number: "))
    print(f"The factorial of {num} is: {factorial(num)}")
except ValueError:
    print("Enter a valid Integer")
