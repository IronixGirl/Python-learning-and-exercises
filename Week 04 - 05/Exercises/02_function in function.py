#Please write a function named square_of_hashes, which draws a square of
#hash characters. The function takes one argument, which determines the
#length of the side of the square.

#The function should call the function line from the exercise above for
#the actual printing out.


def line(x:int):
    print("#"*x)


def box_of_hashes(y:int):
    x = y
    while y > 0:
        line(x)
        y -= 1



if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
