import random


rand = [1,2,3,4,5,5,6,7,8,9]
while len(rand)<=10:
    nwrand = random.choices(rand)
    print(nwrand)
    break