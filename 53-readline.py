# line = open("myfile.txt", "r")
# i = 0
# while True:
#     i = i + 1
#     myline = line.readline()
#     if not myline: 
#         break

#     m1 = myline.split(",")[0]
#     m2 = myline.split(",")[1]
#     m3 = myline.split(",")[2]
#     print(f"The marks of student {i} in Math is {m1}")
#     print(f"The marks of student {i} in Physics is {m2}")
#     print(f"The marks of student {i} in Urdu is {m3}")

    
#     print(myline)

# line.close()

from sys import exception


line = open("myfile.txt", "r")
students = ["Ali", "Hisaan Ahmad", "Zain Ali"]
i = 0
try:
    while True:
        myline = line.readline()
        
        if not myline:
            break
        
        myline = myline.strip()  
        marks = myline.split(",")
        
        if len(marks) < 3:
            raise IndexError("Data is incomplete in the file")
        
        m1 = int(marks[0])
        m2 = int(marks[1])
        m3 = int(marks[2])
        
        print("="*40)
        print(f'Result of Student {students[i]} is : {myline}')
        print("="*40)
        
        # Mathematics
        if m1 >= 50:
            print("Your student is pass In mathematics")
        else:
            print("Your student is fail In mathematics")
        
        # Physics
        if m2 >= 50:
            print("Your student is pass In physics")
        else:
            print("Your student is fail In physics")
        
        # Urdu
        if m3 >= 50:
            print("Your student is pass In urdu")
        else:
            print("Your student is fail In urdu")
        
        print() 
        i += 1

    line.close()
    
except Exception as e:
    print(f"An error occurred: {e}")
    line.close()