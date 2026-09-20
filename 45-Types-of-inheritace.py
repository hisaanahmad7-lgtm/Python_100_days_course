# 1. Single Inheritance

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()


# 2. Multiple Inheritance

class Father:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    def properties(self):
        print(f"The property of Father is {self._p1} and {self._p2}")


class Mother:
    def __init__(self, p3, p4):
        self._p3 = p3
        self._p4 = p4

    def properties(self):
        print(f"The property of Mother is {self._p3} and {self._p4}")


class Child(Father, Mother):
    def __init__(self, p1, p2, p3, p4, skill):
        Father.__init__(self, p1, p2)
        Mother.__init__(self, p3, p4)
        self._skill = skill

    def skills(self):
        print(f"The skill of Child is {self._skill}")


f1 = Father("GOOD man", "Doctor")
f1.properties()

f2 = Father("GOOD girl", "House wife")
f2.properties()

c = Child("Smart", "Kind", "Caring", "Patient", "Coding")
c.properties()
c.skills()


# 4. Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def wheels(self):
        print("4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("2 wheels")

c = Car()
b = Bike()
c.start()
b.start()


# 5. Hybrid Inheritance

class Base:
    def base_method(self):
        print("Base method")

class Parent1(Base):
    def p1(self):
        print("Parent1 method")

class Parent2(Base):
    def p2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    def child_method(self):
        print("Child method")

c = Child()
c.base_method()
c.p1()
c.p2()
c.child_method()
