#Please write a function named no_vowels, which takes a string argument. The
#function returns a new string, which should be the same as the original but
#with all vowels removed.

#You can assume the string will contain only characters from the lowercase
#English alphabet a...z.


def no_vowels(string):
    vowel_var = "aeiou"
    new_string = string
    
    for i in vowel_var:
        if i in string:
            new_string2 = new_string
            new_string = new_string.replace(i,"")
            new_string2 = new_string
            #print(new_string)
        
    return new_string2




my_string = "this is an example"
print(no_vowels(my_string)) #ths s n xmpl



