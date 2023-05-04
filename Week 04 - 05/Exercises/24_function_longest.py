#Please write a function named length_of_longest, which takes a list of
#strings as its argument. The function returns the length of the longest
#string.

my_list = ["first", "second", "fourth", "eleventh"]


def length_of_longest(param_list):
    longest = ""

    for i in param_list:
        if len(i) > len(longest):
            longest = i
    return len(longest)



result = length_of_longest(my_list)
print(result)



        








