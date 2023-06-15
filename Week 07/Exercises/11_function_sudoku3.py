#The function print_sudoku(sudoku: list) takes a two-dimensional array
#representing a sudoku grid as its argument. The function should print out
#the grid in the format specified in the examples below.

#The function copy_and_add(sudoku: list, row_no: int, column_no: int,
#number: int) takes a two-dimensional array representing a sudoku grid,
#two integers referring to the row and column indexes of a single square, and
#a single digit between 1 and 9, as its arguments. The function should return
#a copy of the original grid with the new digit added in the correct location.
#The function should not change the original grid received as a parameter.



# PRINTING SUDOKU
def print_sudoku(sudoku):
    square_cnt = 0
    row_cnt = 0
    
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")

            square_cnt += 1
            if square_cnt == 3 or square_cnt == 6:
                print(" ", end="")
        square_cnt = 0
        print()
        row_cnt += 1
        if row_cnt == 3 or row_cnt == 6:
            print()

# ADDING NUMBERS
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku2 = []
    for row in sudoku:
        row_new = row[:]
        sudoku2.append(row_new)


    sudoku2[row_no][column_no] = number

    return sudoku2

        

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
    print()
    grid_copy2 = copy_and_add(grid_copy,3,4,5)
    print("Copy2:")
    print_sudoku(grid_copy2)


