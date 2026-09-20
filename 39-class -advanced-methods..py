# class Employee:
#     companyName = "Tesla"

#     def __init__(self, name, occo, salary, company):
#         self._name = name
#         self._occo = occo
#         self._salary = salary
#         self._company = company

#     def myIntro(self):
#         print(f"My name is {self._name} i am {self._occo} and my salary is {self._salary} and he is working @ company {self._company}")

#         @classmethod
#         def fromStar(cls, data):
#             parts = data.split("-")
#             for part in parts:
#                 print(part)
#             return cls(parts[0], parts[1], parts[2], parts[3])



# emp1 = Employee("Hisaan Ahmad", "M.L Engineer", 100, "Apple")
# emp1.myIntro()

# emp_data = "Hisaan-12-1200-Housing colony no 2"

# emp2 = Employee.fromStar(emp_data)



class Employee:
    # companyName = "Tesla"

    # def __init__(self, name, occo, salary, company):
    #     self._name = name
    #     self._occo = occo
    #     self._salary = salary
    #     self._company = company

    # def myIntro(self):
    #     print(f"My name is {self._name} i am {self._occo} and my salary is {self._salary} and he is working @ company {self._company}")

    @classmethod
    def fromStar(cls, data):
        parts = data.split("-")
        for part in parts:
            print(part)
        return cls(parts[0], parts[1], parts[2], parts[3])


emp_data = "Hisaan-12-1200-Housing colony no 2"
emp2 = Employee.fromStar(emp_data)
