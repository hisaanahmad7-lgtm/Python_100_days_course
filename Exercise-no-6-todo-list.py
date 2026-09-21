todo_list = []

while True:
    user_choice = input("Enter your Todo: ")
    if user_choice.lower() == "exit":
        break
    todo_list.append(user_choice)

print("Your Todo List:", todo_list)

try:
    while True:
        if not todo_list:
            print("List is empty now!")
            break

        user_pop_choice = input("Enter a Todo item to remove (or 'exit'): ")
        
        if user_pop_choice.lower() == "exit":
            print("Final Todo List:", todo_list)
            break

        if user_pop_choice in todo_list:
            todo_list.remove(user_pop_choice)
            print(f"Removed '{user_pop_choice}'. Updated List:", todo_list)
        else:
            print(f"'{user_pop_choice}' is not in your todo list. Try again.")
            
except KeyboardInterrupt:
    print("\nProgram interrupted. Final Todo List:", todo_list)