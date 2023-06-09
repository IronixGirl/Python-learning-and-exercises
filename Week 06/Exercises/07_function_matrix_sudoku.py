#Please write a function named sudoku_grid_correct(sudoku: list), which takes
#a two-dimensional array representing a sudoku grid as its argument. The
#function should use the functions from the three previous exercises to
#determine whether the complete sudoku grid is filled in correctly. Copy the
#functions from the exercises above into your Python code file for this
#exercise.

#The function should check each of the nine rows, columns and 3 by 3 blocks in
#the grid. If all contain each of the numbers 1 to 9 at most once, the
#function returns True. If a single one is filled in incorrectly, the function
#returns False.

#The image of a sudoku grid above these exercises has the nine blocks within
#the grid indicated with thicker borders. These are the blocks the function
#should check, and they begin at the indexes
#(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).



def sudoku_grid_correct(sudoku: list):

    if row_correct(sudoku) == False:
        return False
    if column_correct(sudoku) == False:
        return False
    if block_correct(sudoku,0, 0) == False:
        return False
    if block_correct(sudoku,0, 3) == False:
        return False
    if block_correct(sudoku,0, 6) == False:
        return False
    if block_correct(sudoku,3, 0) == False:
        return False
    if block_correct(sudoku,3, 3) == False:
        return False
    if block_correct(sudoku,3, 6) == False:
        return False
    if block_correct(sudoku,6, 0) == False:
        return False
    if block_correct(sudoku,6, 3) == False:
        return False
    if block_correct(sudoku,6, 6) == False:
        return False

    return True



#BLOCK-CHECK

def row_correct(sudoku: list):
    row_check = []

    for row in sudoku:
        for num in row:
            if num > 9:
                return False
            elif num == 0:
                continue
            elif num in row_check:
                return False
            else:    
                row_check.append(num)
                print(row_check)

        row_check = []
        
    return True



#COLUMN-CHECK

def column_correct(sudoku: list):
    column_check = []
    loop_cnt = 9
    column_no = 0

    while loop_cnt > 0:
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

        column_check = []
        loop_cnt -= 1
        column_no += 1

    return True




#BLOCK-CHECK

def block_correct(sudoku: list, row_no: int, column_no: int):
    block_check = []
    new_list = []
    num_cnt = 3
    column_cnt = column_no

    for row in sudoku[row_no:row_no+3]:
        while num_cnt > 0:
            new_list.append(row[column_cnt])
            print(new_list)
            num_cnt -= 1
            column_cnt += 1

        num_cnt = 3
        column_cnt = column_no
        

    
    for num in new_list:
        if num > 9:
            return False
        elif num == 0:
            continue
        elif num in block_check:
            return False
        else:    
            block_check.append(num)
            print(block_check)

    return True
        

if __name__ == "__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))#False

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]
    
    print(sudoku_grid_correct(sudoku2))#True



