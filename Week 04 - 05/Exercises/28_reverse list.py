#Please write a function named everything_reversed, which takes a list of
#strings as its argument. The function returns a new list with all of the
#items on the original list reversed. Also the order of items should be
#reversed on the new list.



        

my_list = ["Hi", "there", "example", "one more"]

def everything_reversed(param_list):
    reversed_list = []

    i = len(param_list) - 1
    while i >=0:
        i2 = param_list[i]
        i3 = i2[::-1]
        #print(i3)
        reversed_list.append(i3)
        i -=1
    return reversed_list


new_list = everything_reversed(my_list)


print(new_list) #['erom eno', 'elpmaxe', 'ereht', 'iH']






