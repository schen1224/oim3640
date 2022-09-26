print("ex1:")
# 1.1
def check_fermat(a, b, c, n):
    """
    check if fermat's theorem is correct using parameters.
    """
    if n > 2 and a**n + b**n == c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."


print(check_fermat(2, 4, 6, 4))

# 1.1.2
a = int(input("what is you a>>>"))
b = int(input("what is you b>>>"))
c = int(input("what is you c>>>"))
n = int(input("What is you n>>>"))


def check_fermat(a, b, c, n):
    """
    check if fermat's theorem is correct
    """
    if n > 2 and a**n + b**n == c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."


print(check_fermat(a, b, c, n))

# 1.2.1
def calculate_bmi(weight, height):
    """
    calculating your bmi using parameters weight and height in kg and m
    """
    bmi = weight / (height**2)
    if bmi <= 18.5:
        return "Underweight, eat more!"
    elif 18.5 < bmi <= 25:
        return "Normal weight, you good!"
    elif 25 < bmi < 29.9:
        return "Overweight, eat little bit less!"
    else:
        return "Obesity, eat much less!"


print(calculate_bmi(50, 166))
# 1.2.2
weight = float(input("What is your weight>>"))
height = float(input("What is your height>>"))


def calculate_bmi(weight, height):
    """
    calculating your bmi using parameters weight and height in kg and m
    """
    bmi = weight / (height**2)
    if bmi <= 18.5:
        return "Underweight, eat more!"
    elif 18.5 < bmi < 24.9:
        return "Normal weight, you good!"
    elif 25 < bmi < 29.9:
        return "Overweight, eat little bit less!"
    else:
        return "Obesity, eat much less!"


print(calculate_bmi(weight, height))
print("exercise02:")
