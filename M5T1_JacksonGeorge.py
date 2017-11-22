#CTI 110
#M5T1 - Turtle Graphics
#George Jackson
#10/11/17



# draw a square and a triangle 
import turtle



def main():
    win = turtle.Screen()
    t = turtle.Turtle()

    #add some display options 
    t.pensize(6)            # increase pensize (takes integer)
    t.pencolor("blue")      # set pencolor (takes string) 
    t.shape("turtle")

    #draw a square
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    #separate shapes
    t.penup()
    t.forward(30)
    t.pendown()
    #draw a triangle
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100) 


    






# run the program
main() 






