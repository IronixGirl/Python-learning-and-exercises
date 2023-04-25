#Please write a program which first asks the user for the number of items to
#be added. Then the program should ask for the given number of values, one by
#one, and add them to a list in the order they were typed in. Finally, the
#list is printed out.

new_list = []


item_number = int(input("Give me an amount of items for this list:\n"))


for new_items in range(item_number):
    new_num = int(input("Give me a number for the list:\n"))
    new_list.append(new_num)

print(new_list)






