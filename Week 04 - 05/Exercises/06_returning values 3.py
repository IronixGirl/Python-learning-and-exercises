#Please write three functions: first_word, second_word and last_word. Each
#function takes a string argument.

#As their names imply, the functions return either the first, the second or
#the last word in the sentence they receive as their string argument.

#In each case you may assume the argument string contains at least two
#separate words, and all words are separated by exactly one space character.
#There will be no spaces in the beginning or at the end of the argument strings.


sentence = input("Write a bunch of words:\n")


def first_word(sentence):
    x = sentence.split()
    return x[0]

def second_word(sentence):
    x = sentence.split()
    return x[1]

def last_word(sentence):
    x = sentence.split()
    return x[-1]
    

if __name__ == "__main__":
    #sentence = "it was a dark and stormy python"
    
    print(f"First word: {first_word(sentence)}") # it
    print(f"Second word: {second_word(sentence)}") # was
    print(f"Last word: {last_word(sentence)}") # python
