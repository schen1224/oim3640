# division always gives you a float

import math
from secrets import choice

print(len(str(2 * 100_000)))

import random

print(random.random())  # (0.0-1.0)
print(random, choice(["Sabrina", "Daming", "yy"]))
print(random.randint(0,10))

# \ is a escape character- the one after it is useless
print('I\'m "ok"！')
print("\\n\\\\")
# r to avoid escape character
print(r"\\\n")

# Boolean- only true or false
print(3 > 2)
# or:一个是true都是true
# and: both true 是true
age = 20
type(age >= 21)

age = int(input("what is your age>"))
country = input("what is ur country>")
# age= int(age)
if age >= 21 or country != "USA":
    print("Yes, you can！")
else:
    print("no, you can not!")

    # artimathic>comparison>and or
