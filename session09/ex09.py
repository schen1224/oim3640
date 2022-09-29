import random
name=input('what is your name>>')
realnum=int(random.randint(1,50))
def guess():
    for i in range(1,7):
        num=int(input(('Take a guess>>')))
        if realnum==num:
            return('You are right!')
        elif realnum>=num:
            print(f'higher! you have {6-i}chance')
        else:
            print(f'lower,you have{6-i}chance')
print(guess())

