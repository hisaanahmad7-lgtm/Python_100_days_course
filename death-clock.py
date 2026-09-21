print("Your average age is 70 years! \nKindly enter your answer in percentage (%)")
health = 100

alcohol_consumption = int(input("How much percentage of alcohol you have used in your life: "))
if alcohol_consumption == 0:
    print("Your health is 100% good")
elif alcohol_consumption <= 50:
    health = health - 10
else:
    health = health - 20

drug_addiction = int(input("How much percentage of drugs like (cocaine) you have consumed in your life: "))
if drug_addiction == 0:
    print("Your health is 100% good")
elif drug_addiction <= 50:
    health = health - 10
else:
    health = health - 20

smoking = int(input("How many packets of cigarettes do you consume in 1 week? (Enter answer between 1-10): "))
if smoking == 0:
    print("Your health is 100% good")
elif smoking <= 5:
    health = health - 10
else:
    health = health - 20

ancestor_age = int(input("Enter the age of your ancestors: "))
if ancestor_age > 70:
    print("Your health is 100% good")
elif ancestor_age <= 50:
    health = health - 10
else:
    health = health - 20

if health >= 80:
    print(f"Your final health score is {health}% - Excellent health!")
elif health >= 60:
    print(f"Your final health score is {health}% - Good health, but needs improvement")
elif health >= 40:
    print(f"Your final health score is {health}% - Average health, consider lifestyle changes")
else:
    print(f"Your final health score is {health}% - Poor health, immediate lifestyle changes needed")