#Please write a function named longest(strings: list), which takes a list of
#strings as its argument. The function finds and returns the longest string in
#the list. You may assume there is always a single longest string in the list.

def longest(strings: list):
    longest_length = 0
    longest_word = ""
    
    for item in strings:
        if len(item)>longest_length:
            longest_word = item
            longest_length = len(item)
            print(longest_word)
            print(longest_length)

    return longest_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hai", "hi there"]
    print(longest(strings)) #howdydoody
