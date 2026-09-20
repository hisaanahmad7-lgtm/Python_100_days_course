def counter():
    x = 1
    print("start")
    yield x
    x += 1
    print("resumed")
    yield x

gen = counter()
print(next(gen))
print(next(gen))






def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

for value in count_up_to(5):
    print(value)




import sys

def normal_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result
    # for t in range(n):
    #     print(t)

def generator_func(n):
    for i in range(n):
        yield i

normal = normal_list(1000000)
gen = generator_func(1000000)

print(sys.getsizeof(normal))
print(sys.getsizeof(gen))





def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
for i in range(6):
    print(next(counter))



squares_list = [x**2 for x in range(5)]
squares_gen  = (x**2 for x in range(5))

print(squares_list)
print(squares_gen)
print(list(squares_gen))




def numbers():
    yield 1
    yield 2
    yield 3

def letters():
    yield 'a'
    yield 'b'

def combined():
    yield from numbers()
    yield from letters()

for item in combined():
    print(item)




def numbers(n):
    for i in range(1, n + 1):
        yield i

def filter_even(gen):
    for num in gen:
        if num % 2 == 0:
            yield num

def square(gen):
    for num in gen:
        yield num ** 2

def take(gen, count):
    for i, value in enumerate(gen):
        if i >= count:
            break
        yield value

pipeline = take(square(filter_even(numbers(1000000))), 5)

for result in pipeline:
    print(result)
