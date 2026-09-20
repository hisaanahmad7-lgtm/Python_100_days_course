
# class person:
#     def __init__(self , n, p):
#         print("Hy i am a good person")
#         self.name = n
#         self.occo = p

#     def info(self):
#         print(f"{self.name} is a {self.occo}")

# a = person("Harry" , "Developer")
# b = person("Ahamd" , "A.I Engennier")
# a.info()
# b.info()


# class students:
#     def __init__(self , n, a, c):
#         self.name = n
#         self.age = a
#         self.course = c

#     def info(self):
#         print(f"{self.name} is {self.age} years old and is enrolled in {self.course} course.")

# c = students("Hisaan", 20, "A.I Engennier")
# c.info()



class character:
    def __init__(self , n , m , o):
        self.name = n
        self.occopation = m
        self.IQ = o
    def intro(self):
        print(f"{self.name} is a {self.occopation} and has an IQ of {self.IQ}")

q1 = character("Nikola Tesla" , "Inventor" , 180)
q2 = character("Issac Newton" , "Physicist" , 162  )
q1.intro()
q2.intro()