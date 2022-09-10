print("Questions 1.1: 5, integer")
print("Question 1.2: NameError")
print("Question 1.3: NameError")
# a=3
# a==5.0 (boolean)
print("Question 1.4: 3, integer")
print("Question 1.5: true, boolean")
print("Question 1.6: true, boolean")
print()
print("Question 2.1: false")
print("Question 2.2: false")
print("Question 2.3: true")
print("Question 2.4: false")
print()


import time

seconds = time.time()
days = seconds // (60 * 60 * 24)
ad = seconds / (60 * 60 * 24)

hours = int((ad - days) * 24)
ah = (ad - days) * 24

minutes = int((ah - hours) * 60)
am = (ah - hours) * 60
actual_seconds = int((am - minutes) * 60)


print(
    f"Question 3: Days:{days} Hours: {hours} Minutes: {minutes} seconds: {actual_seconds}"
)
