#Please write a function named sum_of_positives, which takes a list of
#integers as its argument. The function returns the sum of the positive values
#in the list.

this_list = [1, -2, 3, -4, 5]

def sum_of_positives(this_list):
    a = 0
    for i in this_list:
        if i > 0:
            print(i)
            a += i
    return a
        

result = sum_of_positives(this_list)
print(f"The result is {result}")



        








