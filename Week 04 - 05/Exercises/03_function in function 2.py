#Please write a function named shape, which takes four arguments. The first
#two parameters specify a triangle, as above, and the character used to draw
#it. The first parameter also specifies the width of a rectangle, while the
#third parameter specifies its height. The fourth parameter specifies the
#filler character of the rectangle. The function prints first the triangle,
#and then the rectangle below it.

#The function should call the function line from the exercise above for
#the actual printing out.


def line(x, word1, y, word2):
    if y == 0:
        print(f"{x*word1}")
    elif x == 0:
        print(f"{y*word2}")

def shape(num1, word1, num2, word2):
    x = 1
    y = num2
    while x <= num1:
        line(x, word1,0,0)
        x += 1
    while num2 > 0:
        line(0,0,y, word2)
        num2 -= 1



if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
