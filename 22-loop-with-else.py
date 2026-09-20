# import time

# q1  = int(input("Enter a number : "))
# while(q1<=15):
#     print(q1)
#     q1 = q1 +1
#     if q1 == 10:
#         continue
#     elif q1 == 12:
#         print("Loop is going to break! ")
#         time.sleep(2)
#         break
#     else:
#         print("Exception Error! Value Denied")
# else:
#     print("Whole code is wrong! ")


attempts = 3
correct_password = "cyber_security"

while attempts > 0:
    user_input = input("Please enter the password: ")
    if user_input == correct_password:
        print("Login Successful!")
        break
    attempts -= 1
    print(f"Wrong password! Remaining attempts: {attempts}")
else:
    print("Account Locked! your 3 attempts are completed!.")


prices = [120, 500, -5, 350] 

for price in prices:
    if price < 0:
        print("Error:  nagative value is avalible in list!")
        break
else:
    print("All prices are valid. Invoice can be generated.")