from cmath import sqrt
import math

a=float(input("Enter a number:>>>"))
b=float(input("Enter a number:>>>"))
c=float(input("Enter a number:>>>"))


def qua(a, b, c):
    # this is the quadratic equation solver
    R1 = (-b + sqrt(b**2 - 4 * a * c)) / 2 * a
    R2 = (-b - sqrt(b**2 - 4 * a * c)) / 2 * a
    return R1, R2


print(f"the result of the quadratic equation is", {qua(a, b, c)})
