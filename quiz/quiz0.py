"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
# import math

# earth_weight = float(input("what is your weight on earth>"))


# def moon_weight(earth_weight):
#     """
#     your weight on moon
#     """
#     moon_weight = earth_weight * 0.165
#     return moon_weight


# print(moon_weight(earth_weight))

"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Venus = weight on Earth * 0.904

Notice:
1. You don't have to write pseudo-code before coding the function. However if pseudocode is provided, you will get partial credits even if you Python code is not working.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

earth_weight = float(input("what is your weight on earth>"))
planet = str(input("what is your preferred planet>"))


def weight(earth_weight, planet):
    """
    your weight on any three of the planets of your choices
    """
    if planet == "Moon":
        weight = earth_weight * 0.165
        return weight
    elif planet == "Mars":
        weight = earth_weight * 0.378
        return weight
    elif planet == "Venus":
        weight = earth_weight * 0.904
        return weight
    else:
        return print("IDK")


print(weight(earth_weight, planet))
