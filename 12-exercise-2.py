import random

print("*********** Project of while loop ************")
rand_no = ("select a random number between 1 and 100")
print(rand_no.title())
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