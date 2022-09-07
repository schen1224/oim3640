print("Question 1:")
import math

r = 5
volume_of_a_sphere = (4 / 3) * math.pi * r**3
print(volume_of_a_sphere)

print("Question2:")
print("$", 24.95 * (1 - 0.4) + 3 + 0.75 * 59)

print("Question 3:")
Easy = 8 * 60 + 15
Tempo = 7 * 60 + 12
total = 2 * Easy + 3 * Tempo
total_minute = total // 60
total_second = int(((total / 60) - (total // 60)) * 60)

Leavehr = 6
Leavemin = 52
leavemin = 52 + total_minute
if leavemin > 60:
    Leavehr = Leavehr + int((Leavemin + total_minute) // 60)
    leavemin = leavemin - 60
else:
    Leavehr = Leavehr
    leavemin = Leavemin + total_minute


print(
    "I arrive home at "
    + str(Leavehr)
    + ":"
    + str(leavemin)
    + ":"
    + str(total_second)
)

print("Question 4:")
percentage = (89 - 82) / 82
print(f"the percentage of increase is {percentage:3.1f}%.")
