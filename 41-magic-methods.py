class employee:
    def __init__(self , name , occo , salary):
        self._name = name
        self._occo = occo
        self._salary =  salary

    def __str__(self):
        print(f"THe name of Employee is {self._name} his Occopation is {self._occo} and his salary is {self._salary}")

emp1 = employee("Hisaan Ahmad" , "M.L Engennier" , 100)
emp1.__str__()




class Classroom:
    def __init__(self, students , NoOfStudents):
        self.students = students
        self._NoOfStudents = NoOfStudents


    def __len__(self):
        return len(self.students)

c = Classroom(["Ali", "Sara", "Hisaan"] , [12,121,21,21 , 456,  100])
print(len(c))
print(c)





class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

    def __str__(self):
        return f"Rs. {self.amount}"

w1 = Wallet(500)
w2 = Wallet(300)
w3 = w1 + w2
print(w3)




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(2, 3)
p2 = Point(2, 3)
print(p1 == p2)