#Please write a program which asks the user to type in values and adds them to
#a list. After each addition, the list is printed out in two different ways:

#-in the order the items were added
#-ordered from smallest to greatest

#The program exits when the user types in 0.

new_list = []


while True:
    new_item = int(input("Type a number. 0 will end the cycle.\n"))
    
    if new_item == 0:
        print("Bye!")
        break

    else:
        new_list.append(new_item)
        print(f"The list is now: {new_list}")
        print(f"The list in order: {sorted(new_list)}")
        








