import random

#do loop
q1 = "Hy! I am Hisaan Ahmad"
for char in q1:
    print(len(char))
    print(char)

for num in range(20):
    print(f"{num}")
    if num==5:
        print("Hy! i am 5!")
    elif num>50:
        print("I am not 5")


user = int(input("Enter a number---->> : "))
while user>0:
    user = user - 1
    print(f"Number decrease by 1 is : {user}")

l1 = ["Sin0" , "Cos0" , "Tan0" , "sec0" , "cosec0" , "cot0"]
for name in  l1:
    print(name)
    if name == "Cos0":
        print("Hy i am Cos0 my value is one")

print("For loop is executed successfuly")




#While loop

q1 = int(input("Enter a number :"))
q2 = 0
while q2<=10:
    print(f"{q1} x {q2} = ", q1*q2)
    q2 = q2 + 1
q3 = "table printed successfuly!"
print(q3.title(), q3)


num = 10
while num<=20:
    print("The valie is" , num)
    num = num + 1



print("*********** Project of while loop ************")

targerNo = random.randint(1, 100)
userChoise = int(input("Enter a number: "))
guees = 0
while userChoise != targerNo:
    if userChoise < targerNo:
        print("You Enter smaller number! Please enter greater no")
        guees = guees + 1
    elif userChoise > targerNo:
        print("You entered greater number! Please enter smaller no")
        guees = guees + 1
    
    userChoise = int(input("Enter number again : "))

print("Congratulations! you entered correct no")
print(f"You try {guees} times to guees correct no!")

#We can also use else with while......