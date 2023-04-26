#Please write a program which asks the user for words. If the user types in a
#word for the second time, the program should print out the number of
#different words typed in, and exit.

new_list = []


while True:
    user_word = input("Type a word. Typing the same word at any time will end the prompt\n")
    word = user_word.lower()
    
    if word in new_list:
        print(f"You typed in {len(new_list)} different words")
        break

    else:
        new_list.append(word)
        








