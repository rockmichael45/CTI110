#CTI 110
#M6HW1 - Test Grading Program 
#George Jackson
#11/6/17



#Write a program that asks the user to enter five test grades.


def main():
    total = 0
    for times in range(1, 6):
        score = int(input('What is your score '))
        print(determine_grade(score))
        letter_grade = determine_grade(score)
        print("Letter grade:", letter_grade) 
        total += score


    average = calc_average(total)

    print ('The average is', average)

def calc_average(total):
    return total / 5

def determine_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    elif 0 <= grade <= 59:
        return 'F' 


main() 
    
    
