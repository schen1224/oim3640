"""
Question 1:

Given 3 integers, a b c, return their sum. However, if two numbers are the
same, only return the other number. If three numbers are the same, return 0.

"""


def sum_uniques(a, b, c):
    """
    Given 3 integers, a b c, return their sum. If two numbers are the same,
    only return the other number. If three numbers are the same, return 0.
    """
    if a==b==c:
        return('0')
    elif a==b:
        return(c)
    elif a==c:
        return(b)
    elif c==b:
        return(a)
    else: 
        result= a+b+c
        return(result)
print(sum_uniques(2,2,2))


# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(sum_uniques(2022, 9, 29))
# # expect: 2030
# print(sum_uniques(2022, 9, 9))
# # expect: 2022
# print(sum_uniques(2022, 2022, 2022))
# # expect: 0


"""
-----------------------------------------------------------------------
Question 2:

Write a function with loops that returns the total and the average of cubes 
of all the integers between 1 and n (inclusive).

For example: if n is 5, the total is 1*1*1 + 2*2*2 + ... + 5*5*5 = 225,
the average is 225/5 = 45. The function needs to return 225, 45.
"""


def calc_stats(n):
    """
    Given integer n, return the total and the average of cubes of all the integers between 1 and n (inclusive).
    """
    result=0
    for i in range(1,n+1):
        result += i*i*i
        return result,result/n
print(calc_stats(5))


# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(calc_stats(1))
# # expect: 1, 1.0
# print(calc_stats(5))
# # expect: 225, 45


"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that prints the following pattern.
If n is 5, expected output is:

e
d d
c c c
b b b b
a a a a a

If the above pattern is too difficult, try to print a simpler version:

5
4 4
3 3 3
2 2 2 2
1 1 1 1 1

If the above pattern is too difficult, try to print an even simpler version:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""


def print_pattern(n):
    n = 6
    for i in range(n):
        for j in range(i):
            print(i, end=' ')
        print('')

print(print_pattern(5))



# When you've completed your function, uncomment the
# following lines and run this file to test!


# print_pattern(5)
# # expect:
# # 5
# # 4 4
# # 3 3 3
# # 2 2 2 2
# # 1 1 1 1 1

# print_pattern(9)
# # expect:
# # 9
# # 8 8
# # 7 7 7
# # 6 6 6 6
# # 5 5 5 5 5
# # 4 4 4 4 4 4
# # 3 3 3 3 3 3 3
# # 2 2 2 2 2 2 2 2
# # 1 1 1 1 1 1 1 1 1