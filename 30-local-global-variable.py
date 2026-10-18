# number = 12
# print(number)


# def hello():
#     global  y
#     y = 10
#     global number
#     number = 15
#     print(y)
#     print(number)
#     print("Hello World!")

# hello()
# y= 100
# print(y)

my_number = 10
print(my_number)


def printing_number():
    global n
    n = 1000
    print(my_number)
    print(n)
printing_number()
n = 777
print(n)
print(my_number)
