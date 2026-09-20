import this

q1 = {12,33,44,66,91,12}
print(q1)

#Repeted values are not printed in set
qq1 = {}
print(f"The type of {qq1} is = " ,type(qq1))

aa1 = set()
print(type(aa1))
qq2 = {1}
print(f"The type of {qq2} is = " , type(qq2))

for num in q1:
    print(num)

fav_subjects = {"AI", "Cyber Security", "Programming" , "ML Engennier"}
for sub , types in (enumerate(fav_subjects)):
    print(f"The  {types} is Located @ position :{sub} ")


my_skills = {"Linux", "Python"}

my_skills.add("Networking")
print(my_skills)

my_skills.remove("Linux")
print(my_skills)

my_skills.discard("Java")
print(my_skills)

my_skills.clear()
print(my_skills)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

sab_items = set_a.union(set_b)
print(sab_items)

common_items = set_a.intersection(set_b)
print(common_items)

farq_items = set_a.difference(set_b)
print(farq_items)


# issubset(): Yeh check karta hai ke kya ek chote set ke saare items bade set me maujood hain ya nahi. Yeh hume True ya False jawab deta hai.
big_set = {1, 2, 3, 4, 5}
small_set = {2, 4}

print(small_set.issubset(big_set))

print(small_set.issuperset(small_set))
import pandas as pnd

mySet = {12,12,12,12,33,44,"Hisaan","Zain","Ali"}
print(len(mySet))
for set in mySet:
    if len(mySet) == 7:
        print("Wow Awsome!")
    else:
        print(set)

qq1 = pnd.DataFrame(mySet)
print(qq1)

mynewset = {1,2,3}
newSet = {12, 22 , 2, 44  , "Zain" , "Ahmad"}
print(newSet)
q11 =newSet.difference()
print(q11)