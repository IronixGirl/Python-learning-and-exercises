#Please write a function named block_correct(sudoku: list, row_no: int,
#column_no: int), which takes a two-dimensional array representing a sudoku
#grid, and two integers referring to the row and column indexes of a single
#square, as its arguments. Rows and columns are indexed from 0.

#The function should return True or False depending on whether the 3 by 3
#block to the right and down from the given indexes is filled in correctly.
#That is, whether the block contains each of the numbers 1 to 9 at most once.

#Notice that this function does not strictly follow the rules of sudoku. In a
#real game of sudoku there are only 9 blocks to check, and these are located
#at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and
#(6, 6). Such restrictions on indexes should not be implemented here.

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

    print(block_correct(sudoku, 0, 0))#False
    print(block_correct(sudoku, 1, 2))#True
