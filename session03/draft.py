Easy = 8 * 60 + 15
Tempo = 7 * 60 +12
total = 2 * Easy + 3 * Tempo
##print(total)
total1 = total // 60
total2 = int(((total / 60) - (total // 60)) * 60)
##print(total1)
##print(total2)

Leavehr = 6
Leavemin = 52
leavemin = 52 + total1
if leavemin > 60:
     Leavehr = Leavehr + int(( Leavemin + total1) // 60)
     leavemin = leavemin - 60
else:
     Leavehr = Leavehr
     leavemin = Leavemin + total1


print('I arrive home at ' + str(Leavehr) + ':' + str(leavemin) + ':' + str(total2) + " AM.")