import time

def countdown(n):
    ''' i am a doc string'''
    while n >= 0:
        print("Time remaines is " , n)
        n = (n-1)
        time.sleep(1)
    else:
        print("Blast off! " , __doc__)
countdown(5)


def factorial(n):
    if n==1 or n == 0:
        return 1
    else:
         return n * (factorial(n - 1))

q1 = int(input("Enter a number which you want to find factorial : "))
print(factorial(q1))

# F string

a1 = int(input("Enter a first number: "))
b1 = 0
while(b1<=10):
    print(f"{a1} x {b1} = " , a1*b1)
    b1 = b1 + 1