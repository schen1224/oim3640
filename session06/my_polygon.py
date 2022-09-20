from tkinter import N
import turtle

print("exercise01:")
leo = turtle.Turtle()
print(leo)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

for i in range(4):
    leo.fe(100)
    leo.lt(90)

turtle.mainloop()

print("exercise02:")
# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)

# square(leo)
# raphael = turtle.Turtle()
# square(raphael)

# generalization
# def square(t, length):
#     for i in range (4):
#         t.fd(length)
#         t.lt(90)
# square(leo,100)

# def polyline(t,n,length, angle):
#     angle = 360/n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# # polygon(leo,n= 7,length= 70)

# def polyine(t,n,length):
#     angle = 360/n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

import math

# def circle(t,r):
#     circumference = 2 * math.pi * r = 50
#     n = int(arc_length / 3) +1
#     length = circumference / n
#     step_length= arc_length / n
#     step_angle= angle/n


def polyline(t, n, length, angle):
    """
    it shows a line with the desired length and angle. t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """
    it shows n-sided polygon with the input length. t is a turtle.
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """
    it shows the arc with radius r and angle. t is a turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """
    A circle radius r. t is a turtle.
    """
    arc(t, r, 360)


print("exercise03:")
# 01:
def square(t, length):
    """
    draw squares with length
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def special(t, length, a2):
    """
    a special shape with 60 squares, turning right a2 degrees after each square.a1=90
    """
    for i in range(60):
        square(t, length)
        t.lt(a2)


raphael = turtle.Turtle()
special(raphael, 100, 5)
special(raphael)

# 02:

length = input('what is the length>')

def square(t, length):
    """
    draw squares with length of 40
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def special02(t, angle, length):
    """
    squares with 40 length and increment of 4 unites
    """
    for i in range(60):
        square(t, i * 4 + length) 
        # length +=4
        t.lt(angle)


raphael = turtle.Turtle()
special02(raphael, 5, 40)
special02(raphael)

# 03:not sure where goes wrong
def triangle(t, length, angle):
    """
    triangle with any length and angle
    """
    for i in range(3):
        t.fd(length)
        t.lt(angle)


def special03(t, length, angle, angle2, increment):
    """
    spiral with 60 triangle with any angle and increment.
    """
    for i in range(60):
        triangle(t, angle, length + i * increment)
        t.lt(angle2)


raphael = turtle.Turtle()
special03(raphael, 60, 60, 5, 5)
special03(raphael)

# 04
def individual(t, length, angle):
    """
    individual shape with any length and angle.
    """
    for i in range(3):
        t.fd(length)
        t.lt(angle)


def special_general(t, length, angle, angle2, increment, n):
    """
    spiral with any length angle and increment. n is number of loops.
    """
    for i in range(n):
        triangle(t, angle, length + i * increment)
        t.lt(angle2)


raphael = turtle.Turtle()
special03(raphael, 60, 60, 5, 5, 60)
special03(raphael)
