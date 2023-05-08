#Please write a function named formatted, which takes a list of floating point
#numbers as its argument. The function returns a new list, which contains each
#element of the original list in string format, rounded to two decimal points.
#The order of the items in the list should remain unchanged.

#Hint: use f-strings to format the floating point numbers into suitable
#strings.


my_list = [1.234, 0.3333, 0.11111, 3.446]

def formatted(param_list):
    shortened_list = []

    for i in param_list:
        i2 = f"{i:.2f}"
        #print(i2)
        shortened_list.append(i2)
    return shortened_list

new_list = formatted(my_list)

print(new_list) #['1.23', '0.33', '0.11', '3.45']



        








