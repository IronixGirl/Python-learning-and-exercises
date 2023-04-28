#Please write a program which asks the user for a positive integer N. The
#program then prints out all numbers between -N and N inclusive, but leaves
#out the number 0. Each number should be printed on a separate line.

while True:
    num = int(input("Type in an integer:\n"))
    if num < 0:
        print("Please give a positive integer.")
    elif num == 0:
        print("Please give a higher integer.")
    else:
        break

for i in range(num*-1,num+1,1):
    if i == 0:
        continue
    else:
        print(i)
        




        








