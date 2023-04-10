#Please write a function named print_many_times(text, times),
#which takes a string and an integer as arguments. The integer argument
#specifies how many times the string argument should be printed out

time = 0

def print_many_times(text, time):
    while time > 0:
        print(text)
        time -= 1
    print()
     # write your code here

# testing the function:
if __name__ == "__main__":
    print_many_times("hi", 5)
    print_many_times("Trying this out", 3)
