#In this exercise you will write a program for printing out grade statistics
#for a university course.

#The program asks the user for results from different students on the course.
#These include exam points and numbers of exercises completed. The program
#then prints out statistics based on the results.

#Exam points are integers between 0 and 20. The number of exercises completed
#is an integer between 0 and 100.

#The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

#When the user types in an empty line, the program prints out statistics. They
#are formulated as follows:

#The exercises completed are converted into exercise points, so that completing
#at least 10% of the exercises grants one point, 20% grants two points, and so
#forth. Completing all 100 exercises grants 10 exercise points. The number of
#exercise points granted is an integer value, rounded down.

#There is also an exam cutoff threshold. If a student received less than 10
#points from the exam, they automatically fail the course, regardless of their
#total number of points.


    
def user_input():
    score_list_raw = []
    while True:
        score = input("Exam points and exercises completed:\n")
        if score == "":
            print(score_list_raw)
            return score_list_raw
        else:
            score_list_raw.append(score)


def score_results(raw_list):
    grade_type = [0,0,0,0,0,0]
    #total_students = 0
    
    for num in raw_list:
        if score_calc(num) < 15:
            grade_type[0] += 1
            print(grade_type)
        elif score_calc(num) < 18:
            grade_type[1] += 1
            print(grade_type)
        elif score_calc(num) < 21:
            grade_type[2] += 1
            print(grade_type)
        elif score_calc(num) < 24:
            grade_type[3] += 1
            print(grade_type)
        elif score_calc(num) < 28:
            grade_type[4] += 1
            print(grade_type)
        elif score_calc(num) < 31:
            grade_type[5] += 1
            print(grade_type)

        #total_students += 1
        #print(total_students)

    grade_average = sum(score_list_adjusted(raw_list)) / len(score_list_adjusted(raw_list))
    pass_percentage = sum(grade_type[1:]) / sum(grade_type)*100

    print("Statistics:")
    print(f"Points average: {grade_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    print(f"  5: {'*'*grade_type[5]}")
    print(f"  4: {'*'*grade_type[4]}")
    print(f"  3: {'*'*grade_type[3]}")
    print(f"  2: {'*'*grade_type[2]}")
    print(f"  1: {'*'*grade_type[1]}")
    print(f"  0: {'*'*grade_type[0]}")


def score_calc(number):
    score_numbers = number.split()
    score1 = int(score_numbers[0])
    score2 = int(score_numbers[1])

    if score1 < 10:
        score_total = 0
    else:
        score_total = score1 + score2//10

    #print(score_total)
    return score_total


def score_list_adjusted(raw_list):

    adjusted_score_list = []

    for num in raw_list:
        
        score_numbers = num.split()
        score1 = int(score_numbers[0])
        score2 = int(score_numbers[1])

        score_total = score1 + score2//10
        
        adjusted_score_list.append(score_total)
        print(adjusted_score_list)
        

    return adjusted_score_list
        
            



    
numbers = user_input()
results = score_results(numbers)






