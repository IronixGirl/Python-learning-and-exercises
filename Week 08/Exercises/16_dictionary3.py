#Please write a function named factorials(n: int), which returns the
#factorials of the numbers 1 to n in a dictionary. The number is the key, and
#the factorial of that number is the value mapped to it.

#A reminder: the factorial of the number n is written n! and is calculated by
#multiplying the number by each integer smaller than itself. For example, the
#factorial of 4 is 4 * 3 * 2 * 1 = 24.


def histogram(word: str):
    new_dictionary = {}
    value = 1

    for letter in word:
        if letter in new_dictionary:
            new_dictionary[letter] += 1
        else:
            new_dictionary[letter] = 0
            new_dictionary[letter] += 1


    for key in new_dictionary:
        print(f"{key} {'*'*new_dictionary[key]}")
    

        

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")


