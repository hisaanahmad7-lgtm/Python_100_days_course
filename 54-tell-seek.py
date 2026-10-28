with open("1st.txt", "r") as file:

    file.seek(10)
    print(file.tell())

    data = file.read(5)
    
    print(data)  

    print("End\n" * 15)