# Print statement
print("Hello World")

# String variables
name = "Hello "
name1 = "Avesh"

# 1. Concatenation
print(name + name1)  # Output: Hello Avesh

# 2. endswith() – checks if string ends with specific characters
print(name1.endswith('kharani'))  # False

# 3. lower() – converts string to lowercase
print(name1.lower())  # avesh

# 4. upper() – converts string to uppercase
print(name1.upper())  # AVESH

# 5. replace() – replaces part of the string
print(name1.replace('vesh', 'man'))  # Aman

# 6. find() – returns index of first match, -1 if not found
print(name1.find('e'))  # 1

# 7. len() – returns length of string
print(len(name1))  # 5
