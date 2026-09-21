from functools import lru_cache
import time 

@lru_cache
def num(n):
    print(f"The value of n is {n}")
    time.sleep(2)

num(3)
num(5)
num(3)
num(5)
num(100)


from functools import lru_cache
import time

@lru_cache
def square(n):
    print(f"Calculating square of {n}")
    time.sleep(2)
    return n * n

print(square(4)) 
print(square(4))   


@lru_cache
def fabnachi_series(n):
    if n == 0:
        time.sleep(2)
        return 0
    elif n == 1:
        time.sleep(2)
        return 1
    else:
        return fabnachi_series(n - 1) + fabnachi_series(n - 2)

print(fabnachi_series(5))
print(fabnachi_series(1))
print(fabnachi_series(4))
print(fabnachi_series(4))
print(fabnachi_series(20))


@lru_cache

def sqrt(n):
    return n*n

mylist = [1,2,3,5,5,6,7,7,8]
print(list(map(sqrt,  mylist)))



print(list(map(lambda y : y*y , mylist)))