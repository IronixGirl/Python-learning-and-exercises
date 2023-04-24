#Please write a function named same_chars, which takes one string and two
#integers as arguments. The integers refer to indexes within the string.
#The function should return True if the two characters at the indexes
#specified are the same. Otherwise, and especially if either of the indexes
#falls outside the scope of the string, the function returns False.


def same_chars(word,num1,num2):
    if num1 > len(word)-1 or num2 > len(word)-1:
        return "False"
    else:
        return word[num1] == word[num2]
    


if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False
