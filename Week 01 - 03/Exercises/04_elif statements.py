# practicing elif statements

# asking for two numbers and an operator. Then do a math equation based on the operator.
num1 = int(input("Give me a number:\n"))
num2 = int(input("Give me another number:\n"))
op_1 = input("Type in an operation (add, subtract, multiply):\n")

op = op_1.capitalize()

if op == "Add":
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == "Subtract":
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == "Multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

else:
    print("You did something wrong.")


# asking for a number and it will converted to Celsius. Print out statement depending on the Celsius number.
f = int(input("Please type in a temperature (F):\n"))

c = (f - 32) * 5/9

print(f"{f} degrees Fahrenheit equals to {c} degrees Celsius.")

if c < 0:
    print("Brr! It's cold in here!")

elif c > 25:
    print("It's too hot. I'm melting!")

else:
    print("It's not too cold and not too hot. It's just right.")
