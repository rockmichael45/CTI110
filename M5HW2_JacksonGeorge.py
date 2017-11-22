#CTI 110
#M5HW2 - Running Total
#George Jackson
#10/13/17


#Calculate a student's total


def main():
    totalScore = 0
    score = 0 


    repeat = True #This is how we're going to decide to loop
    print('Calculate the student\'s total score: ')
    while repeat:
        
        score = int(input('Next score: '))
        if score < 0:
            repeat = False
        else:
            totalScore = totalScore + score
        

    print('Total is: ', totalScore)
        





main()     

    

    
        
    
