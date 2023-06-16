#Please write a function named transpose(matrix: list), which takes a
#two-dimensional integer array, i.e., a matrix, as its argument. The function
#should transpose the matrix. Transposing means essentially flipping the
#matrix over its diagonal: columns become rows, and rows become columns.

#You may assume the matrix is a square matrix, so it will have an equal number
#of rows and columns.

#The following matrix

#1 2 3
#4 5 6
#7 8 9

#transposed looks like this:

#1 4 7
#2 5 8
#3 6 9

#The function should not have a return value. The matrix should be modified
#directly through the reference.


def transpose(matrix: list):
    new_matrix = []
    col_cnt = 0
    loop_cnt = 3

    while loop_cnt > 0:
        segment = []
        for row in matrix:
            segment.append(row[col_cnt])

        col_cnt += 1
        loop_cnt -= 1
        new_matrix.append(segment)

    
    matrix[:] = new_matrix




        

if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    transpose(matrix)
    print(matrix)


