number = 12
print(number)


def hello():
    global  y
    y = 10
    global number
    number = 15
    print(y)
    print(number)
    print("Hello World!")

hello()
y= 100
print(y)
