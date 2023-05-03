#Please write a function named list_sum which takes two lists of integers as
#arguments. The function returns a new list which contains the sums of the
#items at each index in the two original lists. You may assume both lists
#have the same number of items.

a = [1, 2, 3]
b = [7, 8, 9]

def list_sum(list1,list2):
    new_list = []
    index = 0
    for i in list1:
       c = list1[index] + list2[index]
       new_list.append(c)
       index += 1
    return new_list
        

if __name__ == "__main__":
    print(list_sum(a, b)) # [8, 10, 12]



        








