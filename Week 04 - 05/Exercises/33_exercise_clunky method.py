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

total_points = []
grade5 = 0
grade4 = 0
grade3 = 0
grade2 = 0
grade1 = 0
grade0 = 0
score_pass = 0
total_students = 0
grade_average = 0
pass_percentage = 0
    


while True:
    
    score = input("Exam points and exercises completed:\n")
    if score == "":
        grade_average = sum(total_points) / len(total_points)
        pass_percentage = score_pass / total_students*100
        break
    else:
        score_list = score.split()
        score_1 = int(score_list[0])
        print(score_1)
        score_2 = int(score_list[1])
        print(score_2)
        score_total = score_1 + score_2//10
        print(score_total)

        if score_1 < 10:
            grade0 += 1
        elif score_total <= 14:
            grade0 += 1
        elif score_total >= 15 and score_total <= 17:
            grade1 += 1
            score_pass += 1
        elif score_total >= 18 and score_total <= 20:
            grade2 += 1
            score_pass += 1
        elif score_total >= 21 and score_total <= 23:
            grade3 += 1
            score_pass += 1
        elif score_total >= 24 and score_total <= 27:
            grade4 += 1
            score_pass += 1
        elif score_total >= 28 and score_total <= 30:
            grade5 += 1
            score_pass += 1
            

        total_points.append(score_total)
        total_students += 1
        print(total_points)


print("Statistics:")
print(f"Points average: {grade_average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
print(f"  5: {'*'*grade5}")
print(f"  4: {'*'*grade4}")
print(f"  3: {'*'*grade3}")
print(f"  2: {'*'*grade2}")
print(f"  1: {'*'*grade1}")
print(f"  0: {'*'*grade0}")
      






