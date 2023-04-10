#Please write a function named chessboard, which prints out a chessboard
#made out of ones and zeroes. The function takes an integer argument,
#which specifies the length of the side of the board.

def chessboard(num):
    num2 = 1
    length = 1
    while length <= num:
        if length % 2 == 1:
            while num2 <= num:
                if num2 % 2 == 1:
                    print("1", end="")
                    num2+=1
                else:
                    print("0", end="")
                    num2+=1
        else:
            while num2 <= num:
                if num2 % 2 == 1:
                    print("0", end="")
                    num2+=1
                else:
                    print("1", end="")
                    num2+=1
        print()
        num2 = 1
        length += 1
    print()
    # write your code here

# testing the function:
if __name__ == "__main__":
    chessboard(3)
    chessboard(6)
