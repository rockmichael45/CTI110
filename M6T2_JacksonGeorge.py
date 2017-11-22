#CTI 110
#M6T2 - Feet to Inches
#George Jackson
#11/2/17



#Write a program that asks the user to enter a distance in feet, and prints that same distance in inches.


def feet_to_inches(feet):
    return feet * 12

inches = feet_to_inches(1)
inches
print('10 feet is', feet_to_inches(10), 'inches.')

def main():
    feet = int(input('Enter a number of feet: '))
    print(feet, 'equals', feet_to_inches(feet), 'inches.')



main() 
