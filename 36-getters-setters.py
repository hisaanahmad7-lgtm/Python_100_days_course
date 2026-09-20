# class Mycalss:
#     def __init__(self, name):
#         self._name = name 
#     def show(self):
#         print(f"Name is {self._name} ")
#     @property
#     def value(self):
#         return self._value

# obj = Mycalss("Hisaan")      
# obj.show()


# class myintro:
#     def __init__(self , n , m ,o):
#         self.name = n
#         self.occo = m
#         self.age = o
#     def intro(self):
#         print(f"{self.name} is a good {self.occo} and his/her age is {self.age}")
# newobj = myintro("Hisaan" , "A.I Engennier" , 18)
# newobj.intro()


# class employee:
#     def __init__(self , m , n):
#         self._name = m
#         self._occo = n

#     def intro(self):
#         print(f"{self._name} is good {self._occo}")

#     @property
#     def My_intro(self):
#         return 5*self._name
#     @My_intro.setter
#     def My_intro(self , new_value):
#         self.My_intro = new_value/4

# q1 = employee("Hisaan" , "ML Engennier")
# q1.intro()
# print(q1._name)
# print(q1._occo)
# print(q1.My_intro)

class emp_salary:
    def __init__(self , emp1 , emp2 , emp3):
        self._emp1  = emp1
        self._emp2 = emp2
        self._emp3 = emp3

    def emp_salary_info(self):
        print(f"The salary of 1st emp is {self._emp1} , 2nd is {self._emp2} , 3rd is {self._emp3}")
    @property
    def emp_getter(self):
        return self._emp3 , self._emp1 , self._emp2

    @emp_getter.setter
    def emp_setter(self , value):
        if value <= 10000:
            raise ValueError("Salary is too low enter salary more than 10000")
        self._emp1 = value

    @staticmethod
    def sqrt(n):
        return n*n*n

myemp = emp_salary(500000 , 40000 , 20000)
myemp.sqrt(3)
myemp.emp_salary_info()