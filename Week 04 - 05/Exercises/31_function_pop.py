#Please use the isupper method to write a function named no_shouting, which
#takes a list of strings as an argument. The function returns a new list,
#containing only those items from the original which do not consist of solely
#uppercase characters.

#The Python string method isupper() returns True if a string consists of only
#uppercase characters.



my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]


def no_shouting(some_list):
    shortened_list = []
    for i in some_list:
        print(i)
        if i.isupper() == False:
            shortened_list.append(i)

    return shortened_list

pruned_list = no_shouting(my_list)
print(pruned_list) #['def', 'lower', 'another lower', 'Capitalized']





