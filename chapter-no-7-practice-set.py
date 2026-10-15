# Problem no 1 

# num = int(input("Enter a number: "))
# num2 = 0
# while num2 <= 10:
#     print(f"{num} x {num2} = {num * num2}")
#     num2 += 1


# Problem no 2 

# l1 = ["Hisaan" , "Ali" , "Hassan" ,  "Ahsan" , "Haris" , "Ali" , "Ali" , "Ahmad" , 'Zain' , "FAiz"  ,"Farooq" , "Babar Azam"  ,"Hasseb-ullah"
# ]

# for num in l1:
#     if num.startswith("H"):
#         print(num)
    


# Problem no 3 
# Written with Gemenai 

# l1 = ["Hisaan", "Ali", "Hassan", "Ahsan", "Haris", "Ali", "Ali", "Ahmad", "Zain", "Faiz", "Farooq", "Babar Azam", "Hasseb-ullah"]

# index = 0
# total_elements = len(l1)

# while index < total_elements:
#     name = l1[index]
#     if name.startswith("A"):
#         print(name)
#     index += 1

    # Problem no 4 

# q1 = int(input("Enter a number: "))
# if q1 % 2 == 0:
#     print(f"{q1} is an even number.")
# else:
#     print(f"{q1} is an odd number.")


# Problem no 5 

# i = 1
# sum = 0
# while i <= 4:
#     # sum = sum + 1
#     sum = sum + i
#     i = i + 1


# print("The sum of numbers from 0 to 4 is:", sum)

# Problem no 10

# num = int(input("Enter a number: "))
# num2 = 10
# while num2 >= 1:
#     print(f"{num} x {num2} = {num * num2}")
#     num2 -= 1



# Problem no 6 

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# user_input = int(input("Enter a number to calculate its factorial: "))
# # result = factorial(user_input)
# print(f"Factorial of {user_input} is: " , factorial(user_input))


# Problem no 7 

# for i in range(1, 6):
#     for j in range(i):
#         # i = i-1
#         print("*", end="")


# # Problem no 8
# for i in range(1 , 4):    
#     if i == 1:
#         print(" *  *")
#     else:
#         print("* * *")

# # Problem no 9

for i in range(1, 6):
    for j in range(6 - i):
        print("*", end="")
    print() 


print("\n")
for i in range(1, 6):
    for j in range(0 + i):
        print("*", end="")
    print() 
