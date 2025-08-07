# TCS NQT Question: Count vowels and consonants in a string

def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v_count = 0
    c_count = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    print("Vowels:", v_count)
    print("Consonants:", c_count)

# Example input
user_input = input("Enter a string: ")
count_vowels_consonants(user_input)

# TCS NQT Question: Find the second largest number in a list

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))  # remove duplicates
    if len(unique_numbers) < 2:
        print("Second largest not found.")
    else:
        unique_numbers.sort(reverse=True)
        print("Second Largest:", unique_numbers[1])

# Example input
nums = list(map(int, input("Enter numbers separated by space: ").split()))
find_second_largest(nums)
