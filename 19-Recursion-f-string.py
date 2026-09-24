# import time

# def countdown(n):
#     ''' i am a doc string'''
#     while n >= 0:
#         print("Time remaines is " , n)
#         n = (n-1)
#         time.sleep(1)
#     else:
#         print("Blast off! " , __doc__)
# countdown(5)


# def factorial(n):
#     if n==1 or n == 0:
#         return 1
#     else:
#          return n * (factorial(n - 1))

# q1 = int(input("Enter a number which you want to find factorial : "))
# print(factorial(q1))

# # F string

# a1 = int(input("Enter the number do you wanna print table: "))
# b1 = 0
# while(b1<=10):
#     print(f"{a1} x {b1} = " , a1*b1)
#     b1 = b1 + 1

# name11 = input("Enter your name : ")
# marks = int(input("Enter your marks : "))
# print(f'How are you {name11} and the marks of student is {marks}')

from typing import Annotated

# Primary Type, Metadata / Constraints
AgeInput = Annotated[int, "Age must be greater than 0"]