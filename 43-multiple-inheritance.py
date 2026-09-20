class Employee:
    def __init__(self, name):
        self._name = name

    def MyInfo(self):
        print(f"The name of Employee is {self._name}")

class Occupation:
    def __init__(self, occo):
        self._occo = occo

    def MyInfo(self):
        print(f"The Occupation of Employee is {self._occo}")

class FinalResult(Employee, Occupation):
    def __init__(self, name, occo):
        self._name = name
        self._occo = occo

class MyFinalResult(Occupation, Employee):
    '''hy how are you'''
    def __init__(self, name, occo):
        self._name = name
        self._occo = occo


emp1 = FinalResult("Hisaan Ahmad", "A.I Engineer")
emp1.MyInfo()
print(FinalResult.mro())

emp2 = MyFinalResult("Ali Raza", "M.L Engineer")
emp2.MyInfo()
print(MyFinalResult.mro().__doc__)