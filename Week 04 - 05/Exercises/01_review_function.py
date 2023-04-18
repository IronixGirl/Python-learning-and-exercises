#Please write a function named line, which takes two arguments:
#an integer and a string. The function prints out a line of text,
#the length of which is specified by the first argument. The character
#used to draw the line should be the first character in the second argument.
#If the second argument is an empty string, the line should consist of stars.

def line(x: int, y: str):
    if y != "":
        print(f"{y[0]*x}")
    else:
        print("*"*x)


if __name__ == "__main__":
    line(7,"%")
    line(10,"LOL")
    line(3,"")
