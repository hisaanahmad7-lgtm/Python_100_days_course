class employee:
    def __init__(self, name, id, phoneNo, Adress):
        self._name = name
        self._adress = Adress
        self._id = id
        self._contactNo = phoneNo

    def info(self):
        print(f"{self._name} is a good person his adress is {self._adress} His id is {self.id} and his contact no is {self._contactNo}")


class myinfo(employee):
    def __init__(self, name, id, phoneNo, Adress, bloodGroup):
        super().__init__(name, id, phoneNo, Adress)
        self._Blood = bloodGroup


class emp_Double_Inheretence(myinfo):
    def __init__(self, DOB, Fathername, name, id, phoneNo, Adress, Blood):
        super().__init__(name, id, phoneNo, Adress, Blood)
        self._dateOfBirth = DOB
        self._fatherName = Fathername

    def emp_Double_Inheretence_info(self):
        print(f"{self._name} is a good person his adress is {self._adress} His id is {self._id} and his contact no is {self._contactNo} his father name is {self._fatherName} and his Blood group is {self._Blood}")


class employee_with_property:
    def __init__(self, m, n):
        self._name = m
        self._occo = n

    def intro(self):
        print(f"{self._name} is good {self._occo}")

    @property
    def My_intro(self):
        return self._My_intro

    @My_intro.setter
    def My_intro(self, new_value):
        self._My_intro = new_value / 4


myemp = employee("Hisaan Ahamd", 464, "03452020147", "Housing Colony no 2")
myemp.info()
print(myemp._contactNo)

myemp2 = myinfo("Ali Raza", 501, "03211234567", "Model Town", "B+")
myemp2.info()
print(myemp2._Blood)

emp3 = emp_Double_Inheretence("15-Aug-1999", "M.Rehan", "Hisaan Ahamd", 464, "03452020147", "Housing Colony no 2", "O+ve")
print(emp3._fatherName, emp3._contactNo)
emp3.emp_Double_Inheretence_info()

test_prop = employee_with_property("Ali", "Engineer")
test_prop.intro()
test_prop.My_intro = 20
print(test_prop.My_intro)


# mynewemp = employee_with_property()
# mynewemp._name = "ALI"                       This will give us error
# mynewemp.intro()