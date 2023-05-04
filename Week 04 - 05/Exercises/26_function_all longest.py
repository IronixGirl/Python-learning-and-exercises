#Please write a function named all_the_longest, which takes a list of strings
#as its argument. The function should return a new list containing the longest
#string in the original list. If more than one are equally long, the function
#should return all of the longest strings.

#The order of the strings in the returned list should be the same as in the
#original.

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]


def all_the_longest(param_list):
    longest = ""
    new_list = []

    for i1 in param_list:
        if len(i1) > len(longest):
            longest = i1

    for i2 in param_list:
        if len(i2) == len(longest):
            new_list.append(i2)

    return new_list



result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']


        








