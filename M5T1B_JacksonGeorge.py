#CTI 110
#M5T1B - Turtle Graphics
#George Jackson
#10/11/17



#draw your initials
import turtle



def main():
    win = turtle.Screen()
    t = turtle.Turtle()

    #add some display options
    t.pensize(8)            # increase pensize (takes integer)
    t.pencolor("red")       # set pencolor (takes string) 
    t.shape("turtle")


    #draw a "G"
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
    #move turtle
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.pendown()

    #draw a "J"
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(30) 
    
    










#run the program 
main() 
