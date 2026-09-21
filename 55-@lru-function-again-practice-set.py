from functools import lru_cache
import time 


@lru_cache(maxsize=None)
def sleep(n):
    time.sleep(n)
    print("Hy Hisaan How are you! ")

sleep(3)
sleep(4)
sleep(3)



@lru_cache(maxsize=None)
def number(n):
    time.sleep(3)
    print(f"your number is {n}")

number(5)
number(10)
number(5)

