from tkinter import N
import turtle
def triangle(t,length,angle=60):
    '''
    triangle with any length and angle
    '''
    for i in range (3):
        t.fd(length)
        t.lt(angle)
    # turtle.penup(length)
    # turtle.pendown
   

def special03(t,length,angle, angle2,increment):
    for i in range(60):
        triangle(t, angle,length + i*increment)
       
        
raphael = turtle.Turtle()
special03(raphael,60,60,5,5)
special03(raphael)



