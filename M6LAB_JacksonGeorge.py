#CTI 110
#M6LAB
#George Jackson
#10/30/17



#Write a program that will ask the user their name and then ask their age.



def main():
    name = input("What is your name")
    greet(name)
    age = float(input("What is your age"))
    print ('You are a: ', ageCategory(age))

def greet(userName):
    print ("Your name is", userName) 


def ageCategory(age):
    #does not work yet!
    

    if age <= 1:
        category = 'Infant'
    elif age < 13:
        category = 'Child'
    elif age < 20:
        category = 'Teenager'
    elif age >= 20:
        category = 'Adult' 

    return category
    


main() 
