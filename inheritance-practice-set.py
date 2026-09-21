class my_char:
    def __init__(self , name , Myclass):
        self._name = name
        self._class = Myclass

    def info(self):
        print(f"{self._name} is a good man studying in {self._class} class!")

class my_new_developed_char(my_char):
    def __init__(self, name, Myclass , hobby , city):
        super().__init__( name , Myclass)
        self._hobby = hobby
        self._city = city

    def Double_inheritace_info(self):
        print(f"{self._name} is a good man studying in {self._class} class! His hobby is {self._hobby} and his adress is {self._city}")


class my_again_new_developed_char(my_new_developed_char):
    def __init__(self, name, Myclass , hobby , city , fatherName , bloodGroup):
        super().__init__( name, Myclass , hobby , city )
        self._fatherName = fatherName
        self._bloodGroup = bloodGroup

    @property
    def my_blood_group(self):
        return self._bloodGroup
    @my_blood_group.setter
    def my_blood(self , myblood):
        self._bloodGroup = myblood

    def Triple_inheritance_info(self):
        print(f"{self._name} is a good man studying in {self._class} class! His hobby is {self._hobby} and his adress is {self._city} his blood group is {self._bloodGroup} and his father name is {self._fatherName}")

q1 = my_char("Hisaan Ahmad" , 12)
q1.info()
q2 = my_new_developed_char("Hisaan Ahmad" , 12 , "Gardning" , "Toba tek Singh")
q2.Double_inheritace_info()
q3 = my_again_new_developed_char("Hisaan Ahmad" , 12  , "Gardning" , "Toba tek Singh" ,"M.Rehan" , "O+ve")
q3.Triple_inheritance_info()

