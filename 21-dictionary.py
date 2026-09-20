q1 = {
    "name" : "Hisaan",
    "class" : 12,
    "Subjects" : "Computer",
    "Title" : "Upper"
}
print(q1)
print(q1.keys())
print(q1.values())

for keys in q1.keys():
    if "name" in q1:
        print("Yes name is avalible! ")
    else:
        print(keys)

for values in q1.values():
    print(values)

for keyys in q1.keys():
    print(keyys)


q2 = {"Class" :12 , "Sub" : "Comp" , "Program" : "Python"}
print(q1.setdefault("Class"))





student = {"name": "Hisaan", "age": 19 , "Subject" : "Computer"}
student["age"] = 20 
print(student)

print(student.pop("name"))
print(student)

#Nested dictionary
students_name = {
    "List_1" : {"Ali" : "Junior_Employ" , "Hisaan" : "Expert" , "Ahmad" : "Senior_Employ" , "Irfan" : "ML_engennier"},
    "List_2" : {"Zain" : "A++" , "Rizwan" : "B_Grade" , "Talha" : "Student" , "Faisal" : "C_Grade"}
}
print(students_name["List_1"]["Ali"])

for student, grade in students_name["List_2"].items():
    print(f"Student: {student}, Grade/Status: {grade}")

students_name["List_2"]["Rehan"] = "Manager"

print(students_name["List_2"])

import pandas as pnd
q1  = pnd.DataFrame(students_name)
print(q1)