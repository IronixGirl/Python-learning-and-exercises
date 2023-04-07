# practicing loops and including conditionals

# asking for two words and then sorting them alphabetically
while True:
    word1input = input("Please type in the 1st word:\n")
    word2input = input("Please type in a different word:\n")

    word1 = word1input.lower()
    word2 = word2input.lower()

    if word1 == word2:
        print("You typed the same word. Please type 2 different words.")

    else:
        break
    

if word1 > word2:
    word1order = word2
    word2order = word1

else:
    word1order = word1
    word2order = word2

print(f"Sorting the words alphabetically, we have {word1order} and then {word2order}\n")


# asking for a number and print statements based on if the number is a multiple of 3 or 5 or both
num = int(input("Please give me a number:\n"))


if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print("No fancy phrases for you today.")
