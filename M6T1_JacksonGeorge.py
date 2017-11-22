#CTI 110
#M6T1 - Kilometer Converter
#George Jackson
#10/25/17



#Write a program that asks the user to enter a distance in kilometer and then converts that distance to miles.


convertedMiles = 0.6214


def main():
    kilometers = float(input('Enter a distance in kilometers: '))
#Variable for kilometers
    show_miles(kilometers)
#Define function for show_miles


def show_miles(km):
    miles = km * convertedMiles

#Print the output of kilometers converted to miles
    print(km, "kilometers equals", miles, "miles") 
    

main() 
