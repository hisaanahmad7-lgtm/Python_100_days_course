from abc import ABC, abstractmethod

# Abstractionin py 

# class Vehicle(ABC): 

#   @abstractmethod
#   def start_engine(self):
#     pass


# class Car(Vehicle):

#   def start_engine(self):
#     print("Car engine started with a push button.")


# class Bike(Vehicle):

#   def start_engine(self):
#     print("Bike engine started with a self-start button.")



# my_car = Car()
# my_car.start_engine()  

# my_bike = Bike()
# my_bike.start_engine()  


# Encapsulation in py 
class BankAccount:

  def __init__(self, owner, balance):
    self.owner = owner
    self.__balance = balance

  @property
  def balance(self):
    return self.__balance

  @balance.setter
  def balance(self, amount):
    if amount >= 0:
      self.__balance = amount
    else:
      raise ValueError("You Entered incorrect value!")


account = BankAccount("Hisaan", 1000)

print(account.balance)

account.balance = 1500
print(account.balance)