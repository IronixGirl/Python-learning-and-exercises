#Please write a function named distinct_numbers, which takes a list of
#integers as its argument. The function returns a new list containing the
#numbers from the original list in order of magnitude, and so that each
#distinct number is present only once.

my_list = [3, 2, 2, 1, 3, 3, 1]


def distinct_numbers(param_list):
    new_list = []

    list_sorted = sorted(param_list)
    for i in list_sorted:
        if i in new_list:
           continue
        else:
            new_list.append(i)
    return new_list
        

if __name__ == "__main__":
    print(distinct_numbers(my_list)) # [1, 2, 3]



        








