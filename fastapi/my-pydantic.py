from pydantic import BaseModel, EmailStr, field_validator , Field
from typing import List, Optional , Annotated

class Employee(BaseModel):
    name: Annotated[str , Field(... , example = ["Hisaan , \"Ahmad , \"Ali"])]
    age: int
    talent: Optional[List[str]] = None
    email: EmailStr
    adress : Optional[Annotated[str , Field(... , examples=['Satelite town' , 'Mujahid Town'] , description="Enter the adress of your house ")]]  = None

    def Info_of_Employee(self):
        print(f"Name: {self.name} | Age: {self.age} | Email: {self.email}")
        if self.talent:
            print(f"Talents: {', '.join(self.talent)}")
        else:
            print("Talents: None")

    @field_validator("email")
    @classmethod
    def validate_email_domain(cls, value: str) -> str:
        allowed_domains = ["name.com", "class.com"]
        domain_name = value.split('@')[-1]
        
        if domain_name not in allowed_domains:
            raise ValueError(f"Domain '{domain_name}' is not allowed. Choose from {allowed_domains}")
        return value  



    @field_validator('age')
    @classmethod
    def correct_age(cls , Myvalue : int) -> int:
        if Myvalue>100 and Myvalue<0:
            return ValueError("Incorrect name, ENter name between (1----100)")
        return Myvalue
    



emp1 = Employee(name="Hisaan Ahmad", age=50,  email="hisaan@name.com")
emp1.Info_of_Employee()

print("---")

emp2 = Employee(name="Zain Ali", age=20, talent=["Worker", "Dancer"], email="zain@class.com")
emp2.Info_of_Employee()