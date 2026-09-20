def greet(n):
    print(f"Short_out to {n}")

q1 = []
while True:
    user_choice = input("Enter a name : ")
    if user_choice == "no":
        break
    q1.append(user_choice)
print(q1)
for name in q1:
    greet(name)