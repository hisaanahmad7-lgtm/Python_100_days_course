
#________________________________SINGLE INHERITANCE___________________________________________

class Animal:
    def colors(self , color):
        # print("This animal is eating food.")
        self.color = color
    def intro_to_animal(self):
        print(f"The color of animal is {self.color}")


class Dog(Animal):
    def mydogs(self , name):
            # print("This animal is eating food.")
            self.name = name
    def name_to_animal(self):
        print(f"The name of animal is {self.name}")
my_dog = Dog()


my_dog.colors("Black")
my_dog.mydogs("Puppit")
my_dog.name_to_animal()
my_dog.intro_to_animal()  
# my_dog.bark()  








# _______________________________Multiple Inheritance_________________________________________

class Mobile:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"The name of mobile is {self.name}")


class InternetMobile:
    def __init__(self, net):
        self.net = net

    def show_net(self):
        print(f"The network of mobile is {self.net}")


class ColorMobile(Mobile, InternetMobile):
    def __init__(self, color , name , net):
        Mobile.__init__(self , name)
        InternetMobile.__init__(self , net)
        self.color = color

    def show_color(self):
        print(f"The color of mobile is {self.color}")


# Object Creation
my_mobile = ColorMobile("Samsung" , "Jazz supper 4G" , "Black")

# Attributes Set Karein
# my_mobile.set_mobile_name("Samsung")
# my_mobile.set_net_type("5G / Jazz")
# my_mobile.set_color("Black")

# Methods Call Karein
my_mobile.show_name()
my_mobile.show_net()
my_mobile.show_color()





class Employee:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"The name of employee is {self.name}")


class Employee1:
    def __init__(self, salary):
        self.salary = salary  

    def myintro(self):
        print(f"The salary of employee is {self._salary}")


class Employee2(Employee, Employee1):
    def __init__(self, jobRole, name, salary):
        Employee.__init__(self, name)
        Employee1.__init__(self, salary)
        self.jobRole = jobRole

    def newintro(self):
        print(f"The job role of employee is {self.jobRole}")


    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self, value):
        if value < 5000 or value > 1000000:
            raise ValueError("Salary must be between 5000 and 1000000")
        self._salary = value


try:
    emp1 = Employee2("M.L Engineer", "Hisaan Ahmad", 10000)

    emp1.intro()
    emp1.myintro()
    emp1.newintro()

    emp1.salary = 50000 
    print(f"Updated salary: {emp1.salary}")

except ValueError as e:
    print(f"Error: {e}")






class student:
    def __init__(self , name , age , school):
        self.name =  name
        self.age = age
        self.school = school


    def Info_of_student(self):
        print(f"The name of student is {self.name} the age of student is {self.age} and the student is studying @ {self.school}")

std = student("Hisaan Ahmad" , 18 , "Punjab Maktab")
std1 = student("Zain Ali" , 18 , "Wah Cant")
# print(std.name)
# print(std.age)
# print(std.school)

# print(std1.name)
# print(std1.age)
# print(std1.school)

std.Info_of_student()
std1.Info_of_student()




#______________________________________MUlTILEVEL INHERITANCE__________________________________

class myCar:
    def __init__(self, carName):
        self.carName = carName

    def intro_to_car_name(self):
        print(f"The company of my car is {self.carName}")



class mymyCar(myCar):
    def __init__(self, carName, carColor):
        myCar.__init__(self, carName)
        self.carColor = carColor

    def intro_to_car_color(self):
        print(f"The color of my car is {self.carColor}")



class mymymyCar(mymyCar):
    def __init__(self, carName, carColor, carDesign):
        mymyCar.__init__(self, carName, carColor)
        self.carDesign = carDesign

    def intro_to_car_Design(self):
        print(f"The design of my car is {self.carDesign}")



car1 = mymymyCar("Civic", "Black", "Sedan")


car1.intro_to_car_name()   
car1.intro_to_car_color()  
car1.intro_to_car_Design() 




#______________________________________ HEIRACHICAL INHERITANCE________________________________


class principle:
    def __init__(self , salary ):
        self.salary = salary

    def intro_to_salary(self):
        print(f"The salary of pinciple is {self.salary}")

class tech1(principle):
    def __init__(self , name , salary , subject):
        super().__init__(salary)
        self.name = name
        self.subject = subject

    def intro_to_tech1(self):
        print(f"The name of my tacher  is {self.name} and the subject of teacher is {self.subject} ")


class tech2(principle):
    def __init__(self , name , salary , subject):
        super().__init__(salary)
        self.name = name
        self.subject = subject

    def intro_to_tech2(self):
        print(f"The name of my teacher is {self.name} and the subject of teacher is {self.subject}")


my_teacher = principle(10000)
principle(my_teacher.intro_to_salary())



my_teacher1 = tech1("Atif ali"  , 10000, "Computer")
principle(my_teacher1.intro_to_tech1())
my_teacher1.intro_to_salary()


my_teacher2 = tech2("Hisaan Ahmad" , 100000000 , "Computer")
principle(my_teacher2.intro_to_tech2())
my_teacher2.intro_to_salary()

print("I am a good boy")

