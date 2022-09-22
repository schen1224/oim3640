from cmath import sqrt
import math

g=(1+5**0.5)/2
integer = int(input('your integer is>>>'))
def feb(integer):
    feb=(g**integer-(1-g)**integer)/ sqrt(5)
    return feb