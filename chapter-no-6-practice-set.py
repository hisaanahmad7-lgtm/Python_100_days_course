# Problem no 1

num1= int(input("Enter a 1st number :  "))
num2 = int(input("Enter a 2nd number :  "))
num3 = int(input("Enter a 3rd number :  "))
num4= int(input("Enter a 4th number :  "))


if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is the largest number ! ")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is the largest number ! ")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} is the largest number ! ")
else:
    print(f"{num4} is the largest number ! ")



# problem no 2

sub1 = int(input("Enter the Total marks of Student ( 1 _____ 555) :  "))
if sub1<200:
    print("You are fail in subject 1 ! ")
else:
    print("You are pass in subject 1 ! ")


# problem no 3

text = "Hy i am Hisaan Ahmad i am a good boy i want to be a data scientist now i am working in company buy now our subscription click here  (1) and make a lot of money"

spam_list = ["buy now" , "make a lot of money" , "click here" , "subscribe this" , "buy this" , "buy now and get 50% off" , "buy now and get 70% off"]

if any(spam_word in text for spam_word in spam_list):
    print("This text is spam ! ")
else:
    print("This text is not spam ! ")




text = "You are a good boy and you are working hard"

spam_list = ["buy now" , "make a lot of money" , "click here" , "subscribe this" , "buy this" , "buy now and get 50% off" , "buy now and get 70% off"]

if any(spam_word in text for spam_word in spam_list):
    print("This text is spam ! ")
else:
    print("This text is not spam ! ")




# problem no 4

name = input("Enter your name :  ")
if len(name)<3:
    print("Name must be at least 3 characters long ! ")
elif len(name)>50:
    print("Name can be a maximum of 50 characters long ! ")
else:
    print("Name looks good ! ")


# problem no 5

l1 = ["Hisaan" , "Ahmad" , "Zain" , "Ali" , "Ahmed" , "Haris" , "Zeeshan" , "Ahsan" , "Hassan" , "Hafiz"]
for name in l1:
    if "Hisaan" in name:
        print(f"{name} is present in the list ! ")
    else:
        print(f"{name} is not present in the list ! ")



# problem no 6

# I Can Do it Eassiy so it is wastage of time for me to do this problem because i can do it in 5 minutes so...


# problem no 7

talking_post = "Hy Harry you are good man you are working hard and you are a good boy and you are a good boy and you are a good and harry is a good teacher he has youtube channel named as @CodeWithHarry and he is a good teacher and he is a good man and"

if "harry" in talking_post:
    print("Yes harry is present in the talking post ! ")
else:
    print("No harry is not present in the talking post ! ")