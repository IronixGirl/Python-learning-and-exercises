#Please write a program which asks the user to choose between addition and
#removal. Depending on the choice, the program adds an item to or removes an
#item from the end of a list. The item that is added must always be one
#greater than the last item in the list. The first item to be added must be 1.

#The list is printed out in the beginning and after each operation.

new_list = []
new_value = 0

print(f"The list is now {new_list}")

while True:
    user_choice = input("a(d)d, (r)emove or e(x)it:\n")
    choice = user_choice.lower()
    
    if choice != "d" and choice != "r" and choice != "x":
        print("Command doesn't compute. Try something else.")
        
    elif choice == "d":
        new_value += 1
        new_list.append(new_value)
        print(f"The list is now {new_list}")

    elif choice == "r" and len(new_list) == 0:
        print("There is nothing to remove. Try another command.")

    elif choice == "r":
        new_value -= 1
        new_list.pop(-1)
        print(f"The list is now {new_list}")

    else:
        print("Bye!")
        break
        








