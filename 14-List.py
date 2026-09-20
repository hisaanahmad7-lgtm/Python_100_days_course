q1 = [12 , 23 , 44 , 55 ,66]
l1 = []
print(type(l1))
print("Empty list " , type(q1))

print(len(q1))
print(q1[0 : 3])
print(q1[1:])
print(q1[:2])
print(q1[3])
print(q1[4])

q11 = "By for loop"
print(q11.center(10))
for char in q1:
    print(char)

w1 = ["Hisaan" , "Ahmad" , "Ali" , "Aryan Kelvin" , "Thomas Alva Edison" , "Nikola Tesla"]
print(w1)
print(w1[:])
for alpha in w1:
    print(alpha)

if "Hisaan" in w1:
    print("Yes Hisaan is avalible in w1")
else:
    print("Hisaan is not avalible in w1")

if "Ali" in w1:
    i = 0
    while(i<=5):
        print(f"The value of {i} is : " , i)
        i = i+1
else:
    print("Ali is not avalible in w1! ")


if "Ali" in w1 and 12 in q1:
    print("Yes both are avalible")
else:
    print("Not avalible! ")

x1 =[ a1 for a1 in range(5) if a1%2 == 0]
print(x1)