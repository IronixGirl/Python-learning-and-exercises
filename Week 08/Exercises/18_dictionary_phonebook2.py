#Please write an improved version of the phone book application. Each entry
#should now accommodate multiple phone numbers. The application should work
#otherwise exactly as above, but this time all numbers attached to a name
#should be printed.

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
#040-5466745
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
            for number in phonebook[search]:
                print(number)
        else:
            print("no number")
    elif num == 2:
        name = input("name: ")
        number = input("number: ")
        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = []
            phonebook[name].append(number)
        print(phonebook)
        print("ok!")
    else:
        print("quitting...")
        break



