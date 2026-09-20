class employee:
    def __init__(self , name , id , adress , salary):
        self._name = name
        self._id = id
        self._adress = adress
        self.__salary = salary

    @property
    def emp_info(self):
        return self._name

    @emp_info.setter
    def emp_info(self , my_salary):
        if self.__salary<40000:
            raise ValueError
        else:
            self.__salary = my_salary

    def info(self):
        print(f"{self._name} is a good boy his ID is {self._id} and his adress is {self._adress} and his salary is {self.__salary}")


q1 = employee("Hisaan Ahmad" , 464 , "Housing colony no 2"  ,50000)
print(q1._employee__salary)
print(q1._name.__dir__())
q1.info()


class library:
    def __init__(self, book1 , book2 , book3) :
        self._book1 = book1
        self._book2 = book2
        self._book3 = book3

    def book_info(self):
        print(f"You have taken {self._book1} , {self._book2} and {self._book3}")

std1 = library(input("Enter the name of book: "))
std1 = library(input("Enter the name of book: "))
std1 = library(input("Enter the name of book: "))
std1.book_info()