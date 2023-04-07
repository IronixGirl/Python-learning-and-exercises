# practicing while loops

# asking for a number and then printing if the number is odd or even
while True:
    num = int(input("Give me a number, negative number stops:\n"))

    if num < 0:
        break

    if num % 2 == 0:
        print("It's even.")
    else:
        print("It's odd.")

print("Combo breaker!\n")


# a never-ending loop if the user doesn't type "Yes". The prompt changes based on number of loops
tally = 0

while True:
    if tally <=5:
        resp_1 = input("Will you go out with me?\n")
    elif tally <=10:
        resp_1 = input("I'm not stopping. Go out with me?\n")
    elif tally <=15:
        resp_1 = input("Go out with me?\n")
    elif tally <=20:
        resp_1 = input("I can loop forever, hehe. PleAsE Go OuT wIth Meeee?!\n")
    else:
        resp_1 = input("PleAssssssE Go OooooouT wIth Meeee?!\n")

    response = resp_1.capitalize()

    if response == "No":
        tally += 1

    elif response == "Yes":
        print("Finally!")
        break

    else:
        tally += 1
        print("I need a clear answer.")


print("You reached the 'Got Roped into it Ending'.\nThere are no other endings.\nEnjoy your life")
