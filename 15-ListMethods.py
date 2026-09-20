l1 = [1, 2, 3 , 12,44,68,90,20] 
print(l1)
l1.append(122)
print(l1)
l1.pop(2)
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print("The reverse of list is = " , l1)

q1 = ["Banana" , "Mango" , "Cherry" , "Pineapple" , "Peach" , "Peach"]
q1.extend("Name")
print(q1)


vowels = ["a", "e", "o", "u"]
vowels.insert(2, "i")  
print(vowels)  

vowels.remove("a")
print(vowels)

data = [1, 2, 3, 4]
data.clear()
print(data)  

abc = ["a", "b", "c"]
abc.reverse()
print(abc)  # Output: ['c', 'b', 'a']


letters = ["H", "i", "s", "a", "a", "n"]
name = "".join(letters)
print(name)  # Output: Hisaan


myList = [1,2,2,2,3,4,4,5,5,6,7,8,9]
if myList[1] == myList[2] or myList[5] == myList[6]:
    print(True)
else:
    print(False)

myLists = [1,2,2,2,3,4,4,5,5,6,7,8,9]
if myLists[1] is myLists[2] or myLists[5] is myLists[6]:
    print(True)
else:
    print(False)
