print ('Jarand5122')

#first declare and initialize variables
grade = 0
total = 0
gradeCount = 0
average = 0.0

grade = int(input("Please enter a grade: "))

while grade !=-1:
    if grade <=100:
        total = total + grade
        gradeCount = gradeCount + 1
    else:
        print ("This grade is not valid")
    grade = input("Please enter a grade: ")
    grade = int(grade)

average = total / gradeCount
print (f'the grade average for {gradeCount} grades is {average}')
    