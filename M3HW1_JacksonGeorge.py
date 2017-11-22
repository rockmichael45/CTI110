#CTI 110
#M3HW1 - Age Classifier
#George Jackson
#9/14/17


#Write a program that asks the user to enter a person’s age. The person should display a message indicating whether the person is an infant, a child, a teenager, or an adult.
#Follow these guidelines:
#If the person is 1 year old or less, he or she is an infant.
#If the person is older than one year, but younger than 13 years, he or she is a child.
#If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#If the person is at least 20 years old, he or she is an adult.


userAge = int(input( "Please enter your age: " ) )

if userAge <= 1:
    print( "You are an infant" )
elif userAge < 13:
    print( "You are an child" )
elif userAge < 20:
    print( "You are a teenager" )
elif userAge >= 20:
    print( "You are an adult" )


