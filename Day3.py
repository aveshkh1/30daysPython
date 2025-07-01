#  Day 3 – Data Structures: List and Tuple

# List: Ordered, Mutable, and can store multiple data types (int, str, float, etc.)
my_list = [1, 2, 3, 4, 5, 6, 7]
print("Original List:", my_list)

# 🔹 Indexing (accessing elements by position)
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Third from end:", my_list[-3])

# 🔹 Slicing (returns a range of elements)
print("Elements from index 1 to 2:", my_list[1:3])      # Excludes last index
print("Elements from index 1 to 5:", my_list[1:6])

# 🔹 List methods
my_list.append(8)             # Adds 8 at the end
my_list.reverse()             # Reverses the list
list_copy = my_list.copy()    # Makes a shallow copy
my_list.sort()                # Sorts in ascending order
my_list.sort(reverse=True)    # Sorts in descending order
my_list.remove(8)             # Removes the first occurrence of 8
my_list.pop(4)                # Removes element at index 4

# Print list after modifications
print("Modified List:", my_list)
print("Copied List:", list_copy)

# 📌 Tuple: Ordered, Immutable collection of items
my_tuple = (1, 2, 3, 5, 3, 5, 35)

# 🔹 Tuple methods
print("Count of 3 in tuple:", my_tuple.count(3))
print("Index of first 3 in tuple:", my_tuple.index(3))
