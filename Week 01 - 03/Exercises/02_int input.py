# practicing int input syntax

# asking user for a year
year = int(input("Which year were you born?\n"))
print(f"Your age at the end of the year of 2023: {2023 - year}\n\n")

# asking user for weight and height and calculating BMI
height = float(input("What is your height?\n"))
weight = float(input("What is your weight?\n"))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}\n\n")

# asking user for a number
number = int(input("Please type a number:\n"))
print(f"{number} times 5 is {number*5}\n\n")

# asking user for name and year
name = input("What is your name?\n")
year2 = int(input("Which year were you born?\n"))
print(f"Hi {name.capitalize()}, you will be {2023-year2} years old at the end of 2023")
