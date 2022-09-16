r1= 3
def area_of_circle(radius): #radius = parameter variable
    "this is docstring. return the area of a circle" #required
    pi = 3.14
    area= pi*radius*radius #pass is a place holder when you do not know what to write
    return area #has to write return, otherwise it will return none
area1=area_of_circle(r1) #take r1 into def 里的radius
area2=area_of_circle(1)#1 is argument
print(area1)


def f():
    print('Hi')
    # return none bc no return
print(f())


import math
print(float(23))
print(round(2.4455, 2))
print(ord('S'))
print(ord('C'))
print(chr(78))

