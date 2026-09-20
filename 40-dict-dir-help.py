class employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def Myintro(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Department: {self.department}")

q1 = employee("Hisaan" , 12 , "C++")
q1.Myintro()
print(q1.__dict__)
print(q1.__dir__())
# print(q1.help())
# print(q1.__getattribute__("name"))
# print(q1.__getattribute__("age"))
print(help(employee))