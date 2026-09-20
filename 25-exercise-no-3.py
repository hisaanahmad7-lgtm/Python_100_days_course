name = []
q1 = input("Enter your name :")

if q1.isalpha() or q1.isdigit():
    for char in q1:
        name.append(char)
    
    name.reverse()
    join_Method = "".join(name)
    print(join_Method)
else:
    print("Invalid input! ")


name = []
q1 = input("Enter your name :")

if q1.isalpha() or q1.isdigit():
    for char in q1:
        name.append(char)
    
    name.reverse()
    join_Method = "".join(name)
    print(join_Method)
else:
    print("Invalid input! ")


def reverse_my_string():
    text = input("Enter text to reverse: ")
    text_list = list(text)
    print(text_list)
    text_list.reverse()
    reversed_text = "".join(text_list)
    print("Reversed Output:", reversed_text)

reverse_my_string()



import random

def random_mix():
    text = input("Enter a word to scramble: ")
    text_list = list(text)
    random.shuffle(text_list)
    scrambled = "".join(text_list)
    print("Scrambled Word:", scrambled)

random_mix()




