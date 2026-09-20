#MAp are given below

from functools import reduce


l1= [1,5,2,8,4,7,2,8,5]
# for char in l1:
#     print(char*char)

def square(n):
    return n*n*n

# def sum(x,y):
#     return x+y

# ll1 = [2,3,4]
# nws = list(map(sum , ll1))
# print(nws)
new_map = map(square , l1)
new_map = list(map(square , l1))
new_map = tuple(map(square , l1))
print(new_map)

#Filters are given below
l2 = [2,6,8,3,5,8,5,12,90,1,32]
def max(q):
    return q>5


fil = filter(max , l2)
fil = list(filter(max , l2))
fil = tuple(filter(max , l2))
print(fil)

#Reduce funtion is given below



def add(x, y):
    return x + y

l3 = [1, 2, 3, 4, 5]
result = reduce(add, l3)
print(result)