class employee:
    CompanySize = 0
    def __init__(self , name , occo , company , salry):
        self._name = name
        self._occo = occo
        self._company = company
        self._salary = salry
    CompanySize += 1
    def InfoOfEmployee(self):
        print(f"The name of employee is {self._name} His occopation is {self._occo} his company sized {self.CompanySize} is {self._company} and his salary is {self._salary} ")

class NewEmployee(employee):
    def __init__(self, name, occo, company, salry , Adress , BloodGroup):
        super().__init__(name, occo, company, salry)
        self._adress = Adress
        self._bloodGroup = BloodGroup

    def InfoOfNewEmployee(self):
            print(f"The name of employee is {self._name} His occopation is {self._occo} his company sized {self.CompanySize} is {self._company} and his salary is {self._salary}  His blood Group is {self._bloodGroup} and his adress is {self._adress}")


    
class MyNewEmployee(NewEmployee):
    def __init__(self, name, occo, company, salry , Adress , BloodGroup , FatherName , ContactNO):
        super().__init__(name, occo, company, salry , Adress , BloodGroup)
        self._fathername = FatherName
        self._contactNo = ContactNO

    def InfoOfAgainNewEmployee(self):
            print(f"The name of employee is {self._name} His occopation is {self._occo} his company sized {self.CompanySize} is {self._company} and his salary is {self._salary}  His blood Group is {self._bloodGroup} and his adress is {self._adress} And his father name is {self._fathername} and his contact no is {self._contactNo}")


    @property
    def SalaryInfo(self):
        return self._salary


    
    @SalaryInfo.setter
    def SalaryInfo(self , values):
        if self._salary<=100:
            raise ValueError("Salary is too low wnter greater amount of salary")
        self._salary = values



emp1 = employee("Hisaan Ahmad" , "A.I Engenieer" , "Pak Robotics" , 5)
emp1._salary = 10
emp1.InfoOfEmployee()


emp2 = employee("Zain Ali" , "M.L Engenieer" , "Pak Robotics" , "100 Rupees")
emp2.InfoOfEmployee()

emp3 = NewEmployee("Hisaan Ahmad" , "A.I Engenieer" , "Pak Robotics" , 5 , "Housing Colony no 2" , "O+ve")
emp3._salary = 10000
print(emp3._salary)
emp3.InfoOfNewEmployee()


emp4 = MyNewEmployee("Hisaan Ahmad" , "A.I Engenieer" , "Pak Robotics" , 5 , "Housing Colony no 2" , "O+ve" , "M.Rehan" , "0345......n")
emp4._salary = 10000
print(emp4._salary)
emp4.InfoOfAgainNewEmployee()