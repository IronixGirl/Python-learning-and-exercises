#Please write a function named double_items(numbers: list), which takes a list
#of integers as its argument.

#The function should return a new list, which contains all values from the
#original list doubled. The function should not change the original list.



def double_items(numbers: list):
    double_list = []

    for num in numbers:
        double_list.append(num*2)


    return double_list

        

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)#original: [2, 4, 5, 3, 11, -4]
    print("doubled:", numbers_doubled)#doubled: [4, 8, 10, 6, 22, -8]



