# practicing loops with elif statements and with strings

# asking the user to input a year and then calculating the next leap year
year = int(input("Please input a year:\n"))
next_year = year

while True:
    if year % 4 == 0:
        next_year += 4
        
        if next_year % 100 == 0 and next_year % 400 == 0:
            break
        elif next_year % 100 == 0:
            next_year += 4
            break
        else:
            break

    else:
        next_year += 1

        if next_year % 4 == 0:
        
            if next_year % 100 == 0 and next_year % 400 == 0:
                break
            elif next_year % 100 == 0:
                next_year += 4
                break
            else:
                break
        

# asking the user to input a word, which will loop until the user writes "end". Then all the words that have been inputted will be printed out
print(f"The next leap year after {year} is {next_year}\n")


story1 = ""

while True:
    word = input("Please type in a word:\n")
    
    if word == "end":
        print(story1)
        break

    story1 += word + " "

# asking the user to input two words, which will loop until the user writes the same word twice. Then all the words that have been inputted will be printed out
story2 = ""

while True:
    word1 = input("Please type in a word:\n")
    story2 += word1 + " "
    
    word2 = input("Please type in a word:\n")
    if word1 == word2:     
        print(story2)
        break
    else:
        story2 += word2 + " "
