from cmath import sqrt


print('exercise01:')
r=0
for i in range(1,11):
    r+=i
print(r)
# range:0123

r=0
def sum1000():
    r=0
    for i in range(1,1001):
        r+=i
    return (r)

def sum_up(n):
    r=0
    for i in range(1, n+1):
        r+=i
    return r
print(sum_up(7))

def sum_odd(n):
    r=0
    for i in range(1,n+1):
        if i%2==1:
            r +=1
        else:
            continue
    return r
print(sum_odd(1000))

print('exercise:2.1.1: Iteration0:count is 1')
print('exercise:2.1.2: Iteration1:count is 2')
print('exercise:2.1.3: Iteration2:count is 3')
print('exercise:2.1.4: Iteration3:count is 4')

print('exercise2.2: all counts will be 12')

print('exercise:2.3.1: 4')
print('exercise:2.3.2:12')
print('exercise:2.3.3: 4')
print('exercise:2.3.4: 1')

print('exercise:3')
print('exercise:3')
import math
epsilon=0.0000000001
def test_square_root(x,a):
    while True:
        print(x)
        y=(x+a/x)/2
        if abs(y-x)< epsilon :
            break
        x=y
    return a, test_square_root, math.sqrt(x), math.sqrt(x)-float(test_square_root)

print(test_square_root(4,3))
