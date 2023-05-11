#Please write a function named most_common_character, which takes a string
#argument. The function returns the character which has the most occurrences
#within the string. If there are many characters with equally many
#occurrences, the one which appears first in the string should be returned.


def most_common_character(string):
    cnt = 0
    new_chara = ""
    
    for i in string:
        new_cnt = string.count(i)
        if new_cnt > cnt:
            new_chara = i
            cnt = new_cnt
        
    return new_chara




first_string = "abcdbde"
print(most_common_character(first_string)) #b

second_string = "exemplaryelementary"
print(most_common_character(second_string)) #e



