# # Problem no 1

# myDict = {
#     "Pencil" : "Kalam",
#     "Light" : "Roshni",
#     "Water" : "Pani",
#     "Book" : "Kitaab",
#     "Gate" : "Darwaza"
# }

# for item in myDict.items():
#     if item[0] == "Pencil":
#         print(f"The Hindi word for {item[0]} is {item[1]}")
#     elif item[0] == "Light":
#         print(f"The Hindi word for {item[0]} is {item[1]}")
#     elif item[0] == "Water":
#         print(f"The Hindi word for {item[0]} is {item[1]}")
#     elif item[0] == "Book":
#         print(f"The Hindi word for {item[0]} is {item[1]}")
#     elif item[0] == "Gate":
#         print(f"The Hindi word for {item[0]} is {item[1]}")


# myDict = {"Pencil": "Kalam","Light": "Roshni","Water": "Pani","Book": "Kitaab","Gate": "Darwaza"}
# for english, hindi in myDict.items():
#     print(f"The Hindi word for {english} is {hindi}")
# word = input("Enter an English word: ")
# meaning = myDict.get(word)
# if meaning:
#     print(f"The Hindi word for {word} is {meaning}")
# else:
#     print(f"Sorry, '{word}' is not in the dictionary.")


# Problem no 2

# num = []
# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
#     if user_input == "exit":
#         break
#     else:
#         num.append(int(user_input))
# print(num)
# q2 = num.count(0)
# print(f"The number of zeros in the list is: {q2}")
# if q2 > 1:
#     print("The list contains more than one zero.")


# Problem no 3
# s1 = {1,2,3,18,"18" ,"Hisaan" , "Ahmad" , 1.5 , 2.5 , 3.5}
# for sets in s1:
#     if isinstance(sets, int):
#         print(f"{sets} is an integer.")
#     elif isinstance(sets, str):
#         print(f"{sets} is a string.")
#     elif isinstance(sets, float):
#         print(f"{sets} is a float.")


# Problem no 4

# s = set()
# s.add(12)
# s.add("12")
# s.add(12.0)
# print(len(s))


# Problem no 5

# s = {}
# print(type(s))  

# Problem no 6
# newDict = {}
# enter_user_input = input("Enter a key-value pair of language (key:value) or type 'exit' to quit: ")
# while enter_user_input.lower() != "exit":
#     try:
#         key, value = enter_user_input.split(":")
#         newDict[key] = value
#     except ValueError:
#         print("Invalid input format. Please enter in the format 'key:value'.")
#     enter_user_input = input("Enter a key-value pair (key:value) or type 'exit' to quit: ")
# print("Final dictionary:", newDict)

my_new_dict = {}
while True:
    user_name_choice = input("Enter a name (or type 'exit' to quit): ")
    user_language_choice = input("Enter a language (or type 'exit' to quit): ")
    if user_name_choice.lower() == "exit" or user_language_choice.lower() == "exit":
        break
    my_new_dict[user_name_choice] = user_language_choice
print("Final dictionary:", my_new_dict)
for name, language in my_new_dict.items():
    print(f"{name} speaks {language}.")