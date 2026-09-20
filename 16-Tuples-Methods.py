q1 = (1,2,3,"Hisaan" , "Ahmad" , "Ali")
print(type(q1))

# q1[0] = "ImmuteAble"
# print(q1[0])


q11 = (11,)
print(type(q11))

if "Hisaan" in q1:
    print("Yes hisaan is avalible in tuple")
else:
    print("Error 404! Hisaan is not found ")

programic_language = ("Java" , "Python" , "C++" , "SQL" , "Java_script")
for languages in programic_language:
    print(languages)
    print(type(languages))

    #Methods of Tuples

    my_tuple = (10, 20, 30, 20, 40, 20)

result = my_tuple.count(20)
print(result)

my_tuple = ("Python", "C", "Cybersecurity", "AI")

position = my_tuple.index("Cybersecurity")
print(position)




t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2
print(combined)


pattern = ("A", "B") * 3
# nw_pattern = list(pattern)
# print(nw_pattern)
print(pattern)

scores = (45, 12, 89, 32)
sorted_scores = sorted(scores)
print(sorted_scores)


values = (15, 88, 42, 5)
print("Min:", min(values))  # Output: 5
print("Max:", max(values))

marks = (80, 85, 90)
print(sum(marks))

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   
print(middle)
print(last)    


names = ("Hisaan", "Ali")
marks = (90, 85)
zipped = tuple(zip(names, marks))
print(zipped)

my_tuple = (11,22,3,4,5,6,77,3212)
my_tuple[0] = 131
print(my_tuple[0])

my_list = [1,3,5,5,778,8,99]
my_list[0] = 12
print(sum(my_list))

myTuple= [1,2,2,2,3,4,4,5,5,6,7,8,9]
if myTuple[1] == myTuple[2] and myTuple[5] == myTuple[7]:
    print(True)
else:
    print(False)
