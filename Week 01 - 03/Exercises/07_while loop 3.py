# practicing loops with boolean expressions

# asking user to type in their password 2 times
password = input("Type in a password:\n")

while True:
    password2 = input("Please repeat the password:\n")
    if password == password2:
        print("User account is created!\n")
        break

    else:
        print("They don't match!\n")

# asking user to input their pin and count the amount of tries
pin_tries = 0

while True:
    pin = int(input("PIN (4 digits):\n"))
    pin_tries += 1

    if pin == 4321:
        if pin_tries == 1:
            print("Correct! And it only took you one attempt!")

        else:
            print(f"Correct! It took you {pin_tries} attempts")

        break


    else:
        print("Wrong. Try again")
    
