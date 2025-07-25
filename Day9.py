#Day9:Questions on file handling
# Q1: Write a Python program to create a new text file and write some lines to it.
with open("sample.txt", "w") as file:
    file.write("This is line one.\n")
    file.write("This is line two.\n")
    file.write("This is line three.\n")

# Q2: Read and display the contents of the file created in Q1.
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Q3: Count the number of words in the file.
with open("sample.txt", "r") as file:
    words = file.read().split()
    print(f"Total number of words: {len(words)}")

# Q4: Append a new line to the existing file.
with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")

# Q5: Read the file line by line and print each line with its line number.
with open("sample.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")

# Q6: Write a program to copy contents from one file to another.
with open("sample.txt", "r") as file1, open("copy_sample.txt", "w") as file2:
    for line in file1:
        file2.write(line)
