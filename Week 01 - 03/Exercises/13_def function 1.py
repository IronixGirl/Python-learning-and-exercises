#Please write a function named mean, which takes three integer arguments.
#The function should print out the arithmetic mean of the three arguments.

def mean(x, y, z):
    sum = (x + y + z)/3
    print(sum)
     # write your code here

# testing the function:
if __name__ == "__main__":
    mean(5, 3, 1)
    mean(10, 1, 1)
