with open("main.txt", "r") as file:

    file.seek(10)
    print(file.tell())

    data = file.read(5)
    
    print(data)  