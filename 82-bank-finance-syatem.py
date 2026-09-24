from pydantic import computed_field , BaseModel , Field
from typing import Annotated

class bank_mgmt_system():
    # name = Annotated[
    #     str,
    #     Field(
    #         ...,
    #         description="Enter your name",
    #         examples=["Hisaan", "Ali", "Ahmad"]
    #     )
    # ]


    # tatal_balance= Annotated[
    #     int,
    #     Field(
    #         ...,
    #         description="Enter your bank balance",
    #         examples=["2787275", "757828", "10000"]
    #     )
    # ]

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self , amount):
        if amount>0:
            self.balance += amount
        else:
            raise ValueError("Incoorecy value....")


    def withDraw(self , amount):
        if amount>0:
            self.balance -= amount
        else:
            raise ValueError("Incoorecy value....")

        
    def info_of_balance(self):
        print(f"Your total bank balance is {self.balance}")

    # @property
    # def balance(self):
    #     return self.balance

    # @balance.setter
    # def balance(self , value):
    #     if value<0 and value>1000000000:
    #         raise ValueError("You entered incorrect value!")
    #     self.balance = value


name1 = bank_mgmt_system("Hisaan AHmad" , 100000)
name1.deposit(200)
name1.withDraw(50)
name1.info_of_balance()