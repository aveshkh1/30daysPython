# Day 5: Loops
# Loops are used to perform repetitive tasks

# --- WHILE LOOP ---

# Print numbers from 0 to 100
i = 0
while i <= 100:
    print(i)
    i += 1

# Multiplication table using while loop
num = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Linear search using while loop
num1 = 45
lst = [55, 66, 77, 99, 44, 45, 33, 12, 15, 17]
idx = 0
while idx < len(lst):
    if lst[idx] == num1:
        print("Number found at index", idx)
        break
    idx += 1
else:
    print("Number not found")

# --- FOR LOOP ---

# Traverse the list using for loop
for i in lst:
    print(i)

# Linear search using for loop
found = False
for idx, val in enumerate(lst):
    if val == num1:
        print("The number found at index", idx)
        found = True
        break

if not found:
    print("The number not found")

# Multiplication table using for loop and range
num2 = 5
for i in range(1, 11):
    print(f"{num2} x {i} = {num2 * i}")
