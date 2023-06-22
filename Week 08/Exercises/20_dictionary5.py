#Please write a function named dict_of_numbers(), which returns a new
#dictionary. The dictionary should have the numbers from 0 to 99 as its keys.
#The value attached to each key should be the number spelled out in words.


def dict_of_numbers():
    new_dictionary = {}

    dict1 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
             11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
             19: "nineteen"}

    dict2 = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
             7: "seventy", 8: "eighty", 9: "ninety"}

    for num in range(100):
        if num < 20:
            new_dictionary[num] = dict1[num]

        else:
            new_num = divmod(num, 10)
            x = new_num[0]
            y = new_num[1]
            if new_num[1] == 0:
                new_dictionary[num] = dict2[x]
            else:
                new_dictionary[num] = dict2[x] + "-" + dict1[y]

    print(new_dictionary)
    return new_dictionary


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])#two
    print(numbers[11])#eleven
    print(numbers[45])#forty-five
    print(numbers[99])#ninety-nine
    print(numbers[0])#zero



