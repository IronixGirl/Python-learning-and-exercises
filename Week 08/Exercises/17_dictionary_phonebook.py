#Please write a phone book application. It should work as follows:

#command (1 search, 2 add, 3 quit): 2
#name: peter
#number: 040-5466745
#ok!

#command (1 search, 2 add, 3 quit): 2
#name: emily
#number: 045-1212344
#ok!

#command (1 search, 2 add, 3 quit): 1
#name: peter
#040-5466745

#command (1 search, 2 add, 3 quit): 1
#name: mary
#no number

#command (1 search, 2 add, 3 quit): 2
#name: peter
#number: 09-22223333
#ok!

#command (1 search, 2 add, 3 quit): 1
#name: peter
#09-22223333

#command (1 search, 2 add, 3 quit): 3
#quitting...

phonebook = {}


while True:
    num = int(input("Command(1 search, 2 add, 3 quit): "))
    if num < 1 or num > 3:
        print("That number is beyond the scope of this exercise.")
    elif num == 1:
        search = input("name: ")
        if search in phonebook:
            print(phonebook[search])
        else:
            print("no number")
    elif num == 2:
        name = input("name: ")
        number = input("number: ")
        phonebook[name] = number
        print(phonebook)
        print("ok!")
    else:
        print("quitting...")
        break



