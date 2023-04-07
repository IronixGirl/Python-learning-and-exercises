# practicing manipulating strings

# asking user to type a phrase and it will print out "-" by the length of the phrase
phrase = "a"

while len(phrase)>0:
    phrase = input("Type in a phrase:\n")
    if len(phrase) > 0:
        print("-"*len(phrase))


# asking user to type a phrase and it will print out the phrase with * as filler until the length is 20
phrase2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
filler = 20

while len(phrase2)>20:
    phrase2 = input("Please type in a string:\n")
    if len(phrase2)>20:
        print(f"The phrase is {len(phrase2)} letters long. I need at maximum 20 letters.")
    else:
        filler = filler - len(phrase2)
        print("*"*filler + phrase2)

# asking user to type a word and it will print a specific design with the word in the center of the design
phrase3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
filler2 = 30

while len(phrase3)>29:
    phrase3 = input("Give me a word:\n")
    if len(phrase3)>29:
        print(f"The phrase is {len(phrase3)} letters long. I need less than 30.")
    else:
        if len(phrase3)%2 == 0:
            filler2 = (filler2 - len(phrase3)) // 2 - 1
            print(f"len of phrase3: {len(phrase3)}")
            print(f"filler2: {filler2}")
            print("*"*30)
            print("*"+" "*filler2 + phrase3 + " "*filler2+"*")
            print("*"*30)
        else:
            filler2 = (filler2 - len(phrase3)) // 2 - 1
            print(f"filler2: {filler2}")
            print(f"len of phrase3: {len(phrase3)}")
            print("*"*30)
            print("*"+" "*filler2+" " + phrase3 + " "*filler2+"*")
            print("*"*30)
