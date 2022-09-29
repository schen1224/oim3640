# always use main
# pythonic:x,y=y,x
# [3,6]  two values in a container
# r=0
# for i in range(1,11):
#     r+=i
# print(r)
# # range:0123

# r=0
# def sum1000():
#     r=0
#     for i in range(1,1001):
#         r+=i
#     return (r)

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
print(sum_odd(5))

# for: if we know how many times we want to do
# while: only when/what to stop

# continue only ignore the one but continue
# break will still print and then stop