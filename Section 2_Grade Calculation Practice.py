#exam practice prompt
#Calculates the overall grade for four equally weighted programming assignments, where each assignment is graded out of 50 points. Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).
#Calculates the overall grade for four equally weighted programming assignments, where assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.
#Calculates the overall grade for a course with three equally weighted exams (graded out of 100) that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50) that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.
exam1_grade = float(input('Enter score on Exam 1 (out of 100):'))
print('Exam 1 Grade (60% Weight):',exam1_grade,'\n')
exam2_grade = float(input('Enter score on Exam 2 (out of 100):'))
print('Exam 2 Grade (60% Weight):',exam2_grade,'\n')
exam3_grade = float(input('Enter score on Exam 3 (out of 100):'))
print('Exam 3 Grade (60% Weight):',exam3_grade,'\n')
prog1_grade = float(input('Enter score on Programming Assignment 1 (out of 50):'))
print('Programming Assignment 1 Grade (40% Weight)', prog1_grade, '\n')
prog2_grade = float(input('Enter score on Programming Assignment 2 (out of 50):'))
print('Programming Assignment 2 Grade (40% Weight)', prog2_grade, '\n')
prog3_grade = float(input('Enter score on Programming Assignment 3 (out of 50):'))
print('Programming Assignment 3 Grade (40% Weight)', prog3_grade, '\n')
prog4_grade = float(input('Enter score on Programming Assignment 4 (out of 50):'))
print('Programming Assignment 4 Grade (40% Weight)', prog4_grade, '\n')

avg_exam_score = ((exam1_grade/100 + exam2_grade/100 + exam3_grade/100)*100)/3
avg_prog_score = ((prog1_grade/50 + prog2_grade/50 + prog3_grade/50 + prog4_grade/50)*100)/4

overall_grade = (avg_exam_score*0.6) + (avg_prog_score*0.4)

print('Your overall grade is:', overall_grade)
