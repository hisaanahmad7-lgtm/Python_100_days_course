q1 = "Hissan Ahmad"
indices = []

for idx, char in enumerate(q1):
    if char == "s":
        indices.append(idx)

print(indices)


fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")



students = ["Hisaan", "Ahmad", "Rehan"]
rank = 0
for  student in students:
    print(f"Rank {rank}: {student}")
    rank+=1


text  = "Python"
for pos , alpha in enumerate(text):
    print(f"{pos} ---> {alpha}")