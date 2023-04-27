#Please write a function named mean, which takes a list of integers as an
#argument. The function returns the arithmetic mean of the values in the list.




def mean(my_list):
    list_sorted = sorted(my_list)
    middle = len(my_list) // 2
    result = list_sorted[middle]
    print(f"The mean value is {result}")





if __name__ == "__main__":
    mean([5,4,2,1,3])
    mean([1,1,1,1])



        








