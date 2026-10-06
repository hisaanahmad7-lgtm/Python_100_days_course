#Problem no 1:
# q1 = 0
# q2 = []
# while q1<=5:
#     a1 = input("Enter name of fruits: ")
#     q2.append(a1)
#     q1 += 1
# print(q2)

#Problem no 2:
# myList = []  
# while True:
#     user_choice = input("Enter the marks of students: ")     
#     if user_choice.lower() == "exit":
#         break          
#     myList.append(int(user_choice))
#     print(myList)
    

# Problen no 3
# myTuple = (1,55,48,56,4,54,5,45,77)
# myTuple[1] and myTuple[2] == 44
# print(myTuple[1] , myTuple[2])

# problen no 4
def sum(n):
    while (len(n)) == 0:
        return n + n
# l1 = [1,2,3,4]
# q1 = l1[0] + l1[1] + l1[2] + l1[3]
# print(q1)


l1 = [1,2,3,4]
q1 =list(map(sum , l1))
print(q1)

# # prolem no 4
# myTuple =  (7,0,8,0,0,9)
# newTuple = myTuple.count(0)
# print(newTuple)