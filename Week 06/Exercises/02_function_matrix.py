#Please write a function named count_matching_elements(my_matrix: list,
#element: int), which takes a two-dimensional array of integers and a single
#integer value as its arguments. The function then counts how many elements
#within the matrix match the argument value.

def count_matching_elements(my_matrix: list, element: int):
    match_cnt = 0
    
    for row in my_matrix:
        for num in row:
            if num == element:
                match_cnt += 1

    return match_cnt

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1)) #3
