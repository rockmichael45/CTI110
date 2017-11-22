#CTI 110
#M5HW1 - Distance Traveled
#George Jackson
#10/13/17



#What is the speed of the vehicle in mph? 


#How many hours has it traveled?


#Hour     Distance Traveled
#1              40
#2              80
#3              120

def main():
    
    vehicleSpeed = float(input("What is the speed of the vehicle: "))
    timeTraveled = int(input("How many hours has it traveled: "))

    print( "Hour", "Distance Traveled" )  
    for currentHour in range(1, timeTraveled + 1):
        distanceTraveled = vehicleSpeed * currentHour
        print( currentHour,distanceTraveled )
        


main()
