q1 = int(input("Enter a number : "))

q2 = ("Yes! you can drive")
q3 = ("You can not drive!")
if q1>=18:
    print(q2.title())
elif q1>18:
    print(q3.title() , q3.isalpha())
    print("\n Yes Yes Yes")
elif q1<1:
    print("You enter Negayive Age! ")
else:
    print("Invalid input!! ")
