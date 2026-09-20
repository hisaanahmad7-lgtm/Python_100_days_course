import os
print("_________First make myfile.txt file write something in it and then execute this code___________")
filename = "myfile.txt"

with open(filename, "w") as file:
    file.write("Python File I/O Demonstration\n")
    file.write("Line 1: Learning file handling.\n")
    file.write("Line 2: Writing and reading data.\n")

lines_to_append = [
    "Line 3: Appending new content.\n",
    "Line 4: Working with lists of text.\n"
]

with open(filename, "a") as file:
    file.writelines(lines_to_append)

print("--- Reading Entire File ---")
with open(filename, "r") as file:
    content = file.read()
    print(content)

print("--- Reading Line by Line ---")
with open(filename, "r") as file:
    for line_number, line_text in enumerate(file, start=1):
        print(f"{line_number}: {line_text.strip()}")

if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    print(f"File Size: {file_size} bytes")

print("File I/O Operations Completed Successfully.")
