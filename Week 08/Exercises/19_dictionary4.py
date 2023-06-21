#Please write a function named invert(dictionary: dict), which takes a
#dictionary as its argument. The dictionary should be inverted in place so
#that values become keys and keys become values.


def invert(dictionary: dict):
    new_dictionary = {}
    
    for key in dictionary:
        new_dictionary[dictionary[key]] = key

    dictionary.clear()

    for key in new_dictionary:
        dictionary[key] = new_dictionary[key]

    return dictionary

        

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)#{"first": 1, "second": 2, "third": 3, "fourth": 4}



