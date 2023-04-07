# practicing if in syntax

# asking user for a word and then it will print out if a, e, or o are found in the word
while True:
    wordinput = input("Type in a string:\n")
    word = wordinput.lower()

    if "a" in word:
        print("a found")
    else:
        print("a not found")
    if "e" in word:
        print("e found")
    else:
        print("e not found")
    if "o" in word:
        print("o found")
    else:
        print("o not found")
