# Day 4: Dictionary Methods
# Dictionary is an unordered collection of key-value pairs

student = {
    "name": "Avesh",
    "age": 22,
    "course": "Data Science"
}

# Accessing values
print(student["name"])

# Using get() to avoid KeyError
print(student.get("age"))
print(student.get("gender", "Not specified"))  # default fallback

# Adding or updating key-value
student["email"] = "avesh@example.com"
student["age"] = 23

# Removing a key-value pair
student.pop("course")  # removes 'course'
del student["email"]   # removes 'email'

# Get all keys, values, and items
print(student.keys())
print(student.values())
print(student.items())

# Set is an unordered collection of unique items

skills_a = {"Python", "SQL", "ML"}
skills_b = {"Python", "Deep Learning", "SQL"}

# Add an element
skills_a.add("Pandas")

# Update with multiple items
skills_a.update(["NumPy", "Tableau"])

# Union
print(skills_a.union(skills_b))

# Intersection
print(skills_a.intersection(skills_b))

# Difference
print(skills_a.difference(skills_b))

# Remove element (raises KeyError if not found)
skills_a.remove("Pandas")

# Discard element (doesn't raise error if not found)
skills_a.discard("Excel")


