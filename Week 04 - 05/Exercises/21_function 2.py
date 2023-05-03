#Please write a function named even_numbers, which takes a list of integers as
#an argument. The function returns a new list containing the even numbers from
#the original list.

def anagrams(word1,word2):
    return sorted(word1) == sorted(word2)
        

my_list = [1, 2, 3, 4, 5]


def even_numbers(my_list):
    even_list = []
    for i in my_list:
        if i%2 == 0:
            even_list.append(i)
            print(even_list)
    return even_list


new_list = even_numbers(my_list)

print("original", my_list)
print("new", new_list)



        








