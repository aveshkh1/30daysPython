# Day 27: List Comprehension
# List comprehension is a way of creating lists
# It's an elegant, compact, and faster method compared to normal loops

# Normal method
l = []
for i in range(1, 101):
    l.append(i)
print("Normal method:", l)

# List comprehension
l = [n for n in range(1, 101)]
print("List comprehension:", l)

# Even numbers using list comprehension
even_numbers = [n for n in range(1, 101) if n % 2 == 0]
print("Even numbers:", even_numbers)

# Strings
s = "hello"
str_com = [ch for ch in s]
print("String comprehension:", str_com)
