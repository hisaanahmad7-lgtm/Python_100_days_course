# Problem no 1:
def greet(name):
    print(f" Hy {name} Good morning")

name = input("Enter your name : ")
greet(name)


#Problen no 2:
def fill_The_blank(name , date):
    print(f"Dear {name} you are selected! \n @ Date {date}")

name = input("Enter your name : ")
date = input("Enter your Date : ")
fill_The_blank(name , date)

#Problem no 3:
x1 = input("Enter your String : ")
if ("  ") in x1:
    print("Double space is present in your string")
else:
    print("Double space is not present in your string")


#Problen no 4:
xx1 = input("Enter your String : ")
if ("  ") in xx1:
        print("Double space is present in your string")
        xx2 = xx1.replace("  " , " ")
        print("Your current string is " , xx2)
else:
        print("Double space is not present in your string")


# Problem no 5:
My_String = "Dear Hisaan, \n\tThis python course is very good , and easy to understand. \nThanks!"
print(My_String)