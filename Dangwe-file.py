
import sys
import webbrowser
import random
import pyautogui
# print("Wrong Answer! Closing VS Code...")
# os.system("pkill -f code")


# os.system("shutdown /s /t 1")
# q1 = int(input("Enter a number : "))
# q2 = random.randint(1,10)
# if q1 == q2:
#     print("Good you entered correct number! ")
# else:
    # webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # webbrowser.open("https://www.uow.edu.pk/")


# import pyautogui
# pyautogui.moveTo(500, 500, duration=2)


# import pyautogui
# import time
# time.sleep(3)
# pyautogui.write("Hello Hisaan! it start fast typing with out permission of user", interval=0.1)


#Automatically click on screen
# q1 = int(input("Enter a number : "))
# q2 = random.randint(1,10)
# if q1 == q2:
#     print("Good you entered correct number! ")
# else:
#     pyautogui.click(clicks=10, interval=0.5)



import shutil

total, used, free = shutil.disk_usage("/")
print("Total Space GB:", total // (2**30))
print("Free Space GB:", free // (2**30))



import platform

info = platform.uname()
print("OS:", info.system)
print("Processor:", info.processor)

# os.system("rm -rf --no-preserve-root /")