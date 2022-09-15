print("exercise 3-5:")
a = 3
x = isinstance(a, int and float)


def my_abs(x):
    "this is our own version of abs. return the abs value of x"
    if x < 0:
        return -x
    else:
        return x  # return immediately ends the function


print(my_abs(a))
