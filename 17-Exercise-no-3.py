import sys
# import os 

corerct = 0

total_amount = 70000000
Permission = input("Are you ready to play game! (yes or no) : ")
if Permission.upper() == "Yes" or Permission.lower() == "yes":
    print("Ok lets start")
    print("Enter option 1 , 2 , 3 , 4")
    user_choise = int(input("Who invent Atomic weapon first :\n 1:Einstine 2:RutherFord\n  3:J.J Thomson  4:J.Robert Openhimer : "))
    if user_choise == 4:
        print("Congratulation! you entered correct answer! ")
        corerct+=1
    else:
        print("Idiot correct option is 4")
        total_amount = total_amount - 17500000
elif Permission.upper()=="No" or Permission.lower() == "no":
    print("You are looser!")
    sys.exit()

user_choise_2 = input("Are you ready for second question (yes or no) :")
if user_choise_2.upper() == "YES" or user_choise_2.lower() == "yes":
    print("Ok lets ready!")
    user_choise = int(input("Which language is mostly used for AI :\n 1:C  2:Python\n  3:HTML  4:Java : "))
    if user_choise == 2:
        print("Congratulation! you entered correct answer! ")
        corerct+=1
    else:
        print("Idiot correct option is 2")
        total_amount = total_amount - 17500000

        # print("Wrong Answer! Closing VS Code...")
        # os.system("pkill -f code")
elif user_choise_2.upper() == "NO" or user_choise_2.lower() == "no":
    print("You are looser!")
    sys.exit()

user_choise_3 = input("Are you ready for third question (yes or no) :")
if user_choise_3.upper() == "YES" or user_choise_3.lower() == "yes":
    print("Ok lets ready!")
    user_choise = int(input("Which tool is used for packet analysis :\n 1:Nmap  2:Burp Suite\n  3:Wireshark  4:John the Ripper : "))
    if user_choise == 3:
        print("Congratulation! you entered correct answer! ")
        corerct+=1
    else:
        print("Idiot correct option is 3")
        total_amount = total_amount - 17500000

elif user_choise_3.upper() == "NO" or user_choise_3.lower() == "no":
    print("You are looser!")
    sys.exit()

user_choise_4 = input("Are you ready for fourth question (yes or no) :")
if user_choise_4.upper() == "YES" or user_choise_4.lower() == "yes":
    print("Ok lets ready!")
    user_choise = int(input("Which OS is best for penetration testing :\n 1:Windows  2:Kali Linux\n  3:macOS  4:Ubuntu : "))
    if user_choise == 2:
        print("Congratulation! you entered correct answer! ")
        print("Game Over! You did a great job!")
        corerct+=1
    else:
        print("Idiot correct option is 2")
        total_amount = total_amount - 17500000

elif user_choise_4.upper() == "NO" or user_choise_4.lower() == "no":
    print("You are looser!")
    sys.exit()

if corerct<=3:
    print(f"You entered {corerct} Time Correct Answer! please work hard and make your_self efficent!\n Thanks! for plying this game")
    print(f"You Won RS : {total_amount}")
else:
    print(f"You entered {corerct} Time Correct Answer \n Your efforts are awsome! \n Thanks for Playing this game! ")
    print(f"You won RS : {total_amount}")