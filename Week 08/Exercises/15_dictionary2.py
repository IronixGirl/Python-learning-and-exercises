#Please write a function named factorials(n: int), which returns the
#factorials of the numbers 1 to n in a dictionary. The number is the key, and
#the factorial of that number is the value mapped to it.

#A reminder: the factorial of the number n is written n! and is calculated by
#multiplying the number by each integer smaller than itself. For example, the
#factorial of 4 is 4 * 3 * 2 * 1 = 24.


def factorials(n: int):
    new_dictionary = {}
    value = 1

    for i in range(1,n+1):
        new_dictionary[i] = value*i
        value = new_dictionary[i]

    print(new_dictionary)
    return new_dictionary

        

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])#1
    print(k[3])#6
    print(k[5])#120


