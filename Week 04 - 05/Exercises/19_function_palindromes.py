#Please write a function named palindromes, which takes a string argument and
#returns True if the string is a palindrome. Palindromes are words which are
#spelled exactly the same backwards and forwards.

#Please also write a main function which asks the user to type in words until
#they type in a palindrome.




def palindromes(word1):
    word2 = word1[::-1]
    if word1 == word2:
        return True
    else:
        return False
        

while True:
    word1 = input("Please type in a palindrome:\n")
   
    a = palindromes(word1)
    if a == True:
        print(f"{word1} is a palindrome!")
        break
    if a == False:
        print("That wasn't a palindrome")
        continue
    
        





        








