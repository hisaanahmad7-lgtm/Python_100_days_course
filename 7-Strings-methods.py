
q1 = ("Introduction to Strings Methods")
print(q1.center(50))
print(len(q1))


q2 = ("Hy i Am Hisaan Ahmad!! And i am AI Engennier!!")
print(q2.capitalize())
print(q2.upper())
print(q2.lower())

q3 = ("Hy hisaan how are you????")
print(q3.rstrip("?"))
print(q3.title())
print(q3.replace("Hisaan" , "Harry"))
print(q3.split("  "))

q4 = ("He Was A Great  x Man!!")
print(q4.isalnum())
print(q4.isdigit())
print(q4.isascii())
print(q4.isprintable())
print(q4.istitle())
print(q4.islower())


print("PyThOn".swapcase())  # Output: pYtHoN
print("Hi".center(10, "-"))  # Output: ----Hi----
print("hello".index("l"))  # Output: 2
print("hello hello".count("ll"))  # Output: 2
print("A".__add__("B"))  # Output: AB