temp = int(input("Enter the temperature: "))

match temp:
    case _ if temp >= 1 and temp <= 20:
        print("Cold weather!")
    case _ if temp < 1:
        print("Too cold to bear weather!")
    case _ if temp > 20 and temp <= 35:
        print("Temperature is moderate!")
    case _ if temp > 35:
        print("Hot temperature!")
    case _:
        print("Invalid input")

#QUICK QUIZ
day_num = int(input("Enter day number (1-7): "))

match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number! Please enter between 1 and 7.")