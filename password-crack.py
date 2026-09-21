import time
from random import choice

pas = input("Enter your password : ")

keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "!", "@", "#", "$",
    "%", "^", "&", "*", ")", "(", "-", "_", "+", "="
]

pwg = ""
attempt = 0

start_Time = time.time()

for i in range(len(pas)):
    guess = ""
    while guess != pas[i]:
        guess = choice(keys)
        attempt += 1
    pwg += guess
    print(pwg)

end_Time = time.time()
total_time = end_Time - start_Time

print(f"The password is {pwg}")
print(f"Total attempts: {attempt}")
print(f"Time taken: {total_time:.4f} seconds")