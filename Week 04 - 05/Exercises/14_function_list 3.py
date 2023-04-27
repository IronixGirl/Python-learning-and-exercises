#Please write a function named range_of_list, which takes a list of integers
#as an argument. The function returns the difference between the smallest and
#the largest value in the list.




def range_of_list(my_list):
    list_sorted = sorted(my_list)
    result = list_sorted[-1] - list_sorted[0]
    print(f"The range of the list is {result}")





if __name__ == "__main__":
    range_of_list([5,4,2,1,3])
    range_of_list([1,1,1,1])



        








