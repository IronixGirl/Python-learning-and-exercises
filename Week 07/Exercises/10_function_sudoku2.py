#The function print_sudoku(sudoku: list) takes a two-dimensional array
#representing a sudoku grid as its argument. The function should print out
#the grid in the format specified in the examples below.

#The function add_number(sudoku: list, row_no: int, column_no: int, number:int)
#takes a two-dimensional array representing a sudoku grid, two integers
#referring to the row and column indexes of a single square, and a single
#digit between 1 and 9, as its arguments. The function should add the digit to
#the specified location in the grid.



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
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

        

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)


