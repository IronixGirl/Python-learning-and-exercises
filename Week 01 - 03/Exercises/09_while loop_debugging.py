# practicing debugging

# asking the user for a limit and then a base number. The base number will be multiplied against 1 and then itself until the sum reaches the limit number
limit = 0
base = 0
num = 1

while limit < 3:
    print(f"limit < 3: {limit < 3}") #debugging. checking if condition is true or false
    limit = int(input("Give me a number!\n"))
    base = limit + 1
    if limit == 0:
        print("That number is too low.")
    elif limit == 1 or limit == 2:
        print("This number is too low.")

while True:
    print(f"base >= limit: {base >= limit}") #debugging. checking if condition is true or false
    base = int(input("Give me a lower number.\n"))
    print(f"Upper limit: {limit}") #debugging. checking the value of limit
    print(f"Base: {base}") #debugging. checking the value of base
    print(f"base > limit: {base > limit}")  #debugging. checking if condition is true or false
    print(f"base >= limit: {base >= limit}")  #debugging. checking if condition is true or false
    if base == 0 or base == 1:
        print("Not this number.")
    elif base >= limit:
        print("I asked for a lower number.")
    else:
        break

print(f"Upper limit: {limit}")
print(f"Base: {base}")

while num <= limit:
    print(num)
    num *= base
    
