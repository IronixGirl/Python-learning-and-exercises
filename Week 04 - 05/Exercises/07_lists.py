#Please write a program which initialises a list with the values
#[1, 2, 3, 4, 5]. Then the program should ask the user for an index and a
#new value, replace the value at the given index, and print the list again.
#This should be looped over until the user gives -1 for the index. You can
#assume all given index values will fall within your list.

new_list = [1,2,3,4,5]

while True:
    index = int(input("Give me a number:\n"))
    value = int(input("Give me another number:\n"))

    if index == -1:
        break
    elif index > len(new_list)-1 or index < -1:
        print("The first number is out of range. Make it lower.")
    else:
        new_list[index] = value
        print(f"Index: {index}")
        print(f"New value: {value}")
        print(new_list)
    


