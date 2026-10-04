# import time

# correct_password = 123456
# total_attempts = 3
# user_password = int(input("Enter your password: "))

# while True:
#     if user_password == correct_password:
#         print("Access granted!")
#         break
#     else:
#         total_attempts -= 1
#     if total_attempts == 0:
#         print("Access denied! No attempts left.")
#         try:
#             for i in range(3, 0, -1):
#                     print(f"Remaining time is : {i} Seconds...")
#                     time.sleep(1)

#         except KeyboardInterrupt:
#             print("Operation cancelled by user.")

#         total_attempts = 3
#     print(f"Incorrect password. You have {total_attempts} attempts left.")
#     user_password = int(input("Enter your password: "))





# l1 = [1,2,3,4,5,6,7,8,9,10,15,18,20,25,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# def is_divisible_by_5(num):
#     return num % 5 == 0
# mylambda = lambda num: num % 5 == 0
# print(list(filter(is_divisible_by_5, l1)))
# print(tuple(filter(mylambda, l1)))



user_choice = input("Enter your choice: ")

try:
    with open(user_choice + ".txt", "r") as file:
        for line in file:
            print(line.strip())
            
except FileNotFoundError:
    print(f"Error: '{user_choice}.txt' naam ki koi file nahi mili.")