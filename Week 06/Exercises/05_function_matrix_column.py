#Please write a function named column_correct(sudoku: list, column_no: int),
#which takes a two-dimensional array representing a sudoku grid, and an
#integer referring to a single column, as its arguments. Columns are indexed
#from 0.

#The function should return True or False, depending on whether the column is
#filled in correctly, that is, whether it contains each of the numbers 1 to 9
#at most once.

def column_correct(sudoku: list, column_no: int):
    column_check = []
    
    for row in sudoku:
        if row[column_no] > 9:
            return False
        elif row[column_no] == 0:
            continue
        elif row[column_no] in column_check:
            return False
        else:    
            column_check.append(row[column_no])
            print(column_check)

    return True
        

if __name__ == "__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

    print(column_correct(sudoku, 0))#False
    print(column_correct(sudoku, 1))#True
