#More questions functions
#Q1WAF to find the maximum of 3 numbers
def max_nums(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
print(f"{max_nums(1,4,5)} is greater")

#Q2:WAF that returns the sum of all numbers from 1 to n
def sum_of_n(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(sum_of_n(5))
#Q3WAF to count the number of vowel in a string
def vowel_count():
    string=input("Enter the string")
    vowels="aeiouAEIOU"
    count=0
    for i in string:
        if i in vowels:
            count+=1
    return count
print(f"number of vowels in string is {vowel_count()}")
#Q4 WAF to reverse a given string
def reverse_str(str):
    return str[::-1]
print(reverse_str("Tanuja"))

#Q5WAF that returns True if the given string is a palindrome
def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]
#Q6WAF to generate a fibonacci series up to terms

def fibonacci(n):
    a,b=0,1
    for _ in range(n):
       print(a,end=" ")
       a, b = b, a + b

fibonacci(4)
print(is_palindrome("AVesh"))