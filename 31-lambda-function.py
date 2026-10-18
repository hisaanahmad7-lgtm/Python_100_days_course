def sqrt(n):
    return n*n*n

print(sqrt(2))

def sum(a,b):
    return a+b
print(sum(2,2))

mylmbdafunction = lambda x,y: x+y
print(mylmbdafunction(2,2))


mylmbdafunction = lambda x,y,z: x+y+z/3
print(mylmbdafunction(2,2,4))


mylmbdafunction = lambda x,y,z: x+y*z/3
print(mylmbdafunction(2,2,4))


def fabo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0;
    else:
        return fabo(n-1) + fabo(n-2)

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(fabo, lists)))