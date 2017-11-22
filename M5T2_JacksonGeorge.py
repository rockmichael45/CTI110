#CTI 110
#M5T2 - Bug Collector
#George Jackson
#10/9/17


#7 days (range?)
#number of bugs
#todaysBugs
#totalBugs


def main():
    totalBugs = 0
    
    #Get the bugs collected for each day.
    for day in range(1, 8):
        print('Enter the bugs collected on day', day)
        bugs = int(input('Total bugs on this day'))
        totalBugs = totalBugs + bugs 

    #Display the total bugs.
    if totalBugs <= 0:
        print ('You collected a total of', total, 'bugs.')
    elif totalBugs >= 0:
        print ('You have collected:,' ,totalBugs, 'Bugs')

main()



