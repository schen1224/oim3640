"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
import math

earth_weight = float(input("what is your weight on earth>"))


def moon_weight(earth_weight):
    """
    your weight on moon
    """
    moon_weight = earth_weight * 0.165
    return moon_weight


print(moon_weight(earth_weight))
