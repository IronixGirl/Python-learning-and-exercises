# practicing if statements

# asking for name and soup portion. If the name is Jerry, don't ask for a portion and say "No soup for you!"
name_1 = input("What's your name?\n")

name = name_1.capitalize()

if name != "Jerry":
    soup = int(input("How many portions of soup?\n"))
    print(f"The total cost is {soup*5.90}")
    print("Next please!")

else:
    print("No soup for you!")

# asking for a number and print the below statements according to the number
num = int(input("Please type in a number:\n"))

if num < 1000:
    print("This number is smaller than 1000")

if num < 100:
    print("This number is smaller than 100")

if num < 10:
    print("This number is smaller than 10")

print("Thank you!")
