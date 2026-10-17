filename = "1st.txt"


with open(filename, "w") as file:
    file.write("Python File I/O Demonstration\n")
    file.write("Line 1: Learning file handling.\n")
    file.write("Line 2: Writing and reading data.\n")

print("File successfully Created..!\n")

my_lines = [
    "Now i am going to be death the destroy of the world...",
    "I'm possible says i am possible..."
]
with open(filename , "a") as my_file:
    my_file.writelines(my_lines)