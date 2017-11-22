#CTI 110
#M3LAB - Debugging
#George Jackson
#9/13/17

#This program takes a number grade and outputs a letter grade.

#system uses 10-point grading scale
A_score = 100
B_score = 90
C_score = 80
D_score = 70
F_score = 0-60
#TO DO: define the rest of the scores


grade = float(input("Enter your grade"))
if grade > 0 and grade < 60:
    print("Your grade is: F")
elif grade > 60 and grade <=70:
    print("Your grade is: D")
elif grade > 70 and grade <=80:
    print("Your grade is: C")
elif grade > 80 and grade <=90:
    print("Your grade is: B")
elif grade > 90 and grade <=100:
    print("Your grade is: A")
else:
    print("Grades are between 0 and 100") #TO DO: finish this 
