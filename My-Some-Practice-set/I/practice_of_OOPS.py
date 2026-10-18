class student:
    def __init__(self, name, adress, classes, rolno):
        self._name = name
        self.adress = adress
        self.classes = classes
        self.rolno = rolno

    def intro_to_student(self):
        print(f"The name of student is {self._name} the adress of student is {self.adress} the class of student is {self.classes} and finally the rol no of student is {self.rolno}")

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, value):
        if value < 0 or value > 16:
            raise ValueError("Invalid classes")
        self._classes = value

class subStudents(student):
    def __init__(self, name, adress, classes, rolno, iqlevel):
        super().__init__(name, adress, classes, rolno)
        self.iqlevel = iqlevel

    def intro_of_subStudents(self):
        print(f"The name of student is {self._name} the adress of student is {self.adress} the class of student is {self.classes} and finally the rol no of student is {self.rolno} and the iq level of student is {self.iqlevel}")

    @property
    def iqlevels(self):
        return self.iqlevel

    @iqlevels.setter
    def iqlevel(self , values):
        if values < 0 or values > 200:
            raise ValueError("Invalid iq_level")
        self.iqlevel = values

q1 = student("Hisaan ahamd", "Housing colony no 2", 13, 130)
q1.intro_to_student()

q2 = subStudents("Hisaan ahamd", "Housing colony no 2", 10, 13, 140)
q2.intro_of_subStudents()