#Given a list of integers, let's decide that two consecutive items in the list
#are neighbours if their difference is 1. So, items 1 and 2 would be
#neighbours, and so would items 56 and 55.

#Please write a function named longest_series_of_neighbours, which looks for
#the longest series of neighbours within the list, and returns its length.

#For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours
#would be [5, 4, 3, 4], with a length of 4.



my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]


def longest_series_of_neighbours(some_list):
    longest = 0
    current_streak = 0
    item = 0
    while item < len(some_list)-1:
        if some_list[item] - some_list[item+1] == 1 or some_list[item] - some_list[item+1] == -1:
            current_streak += 1
            if current_streak > longest:
                longest += 1
        else:
            current_streak = 0
        item += 1
    return longest+1
    



print(longest_series_of_neighbours(my_list)) #4
