# practicing manipulating strings

# asking user for a word and number and multiplying the word that many times
word = input("Give me a word:\n")
num = int(input("Tell me how many times you'd like that word multiplied:\n"))

print(word*num)

# asking for two words and printing which word is longer in length
word1 = input("Give me one word:\n")
word2 = input("Give me another word:\n")

if len(word1)>len(word2):
    winning_word = word1
elif len(word1)<len(word2):
    winning_word = word2

if len(word1)==len(word2):
    print("The words are equally long.")
else:
    print(f"{winning_word} is longer")
