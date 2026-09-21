import random

computer_choice = random.choice(["Snake", "Water", "Gun"])
user_choice = input("Enter your choice (Snake/Water/Gun): ")


user = user_choice.lower()
computer = computer_choice.lower()

if user == computer:
    print(f"Computer chose: {computer_choice}")
    print("It's a tie!")
elif (user == "snake" and computer == "water") or \
     (user == "water" and computer == "gun") or \
     (user == "gun" and computer == "snake"):
    print(f"Computer chose: {computer_choice}")
    print("You win!")
else:
    print(f"Computer chose: {computer_choice}")
    print("Computer wins!")