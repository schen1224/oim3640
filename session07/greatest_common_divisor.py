x = int(input("x input>>"))
y = int(input("y input>>"))


def gcd(x, y):
    if x > y:
        r = y
    else:
        r = x
    for i in range(1, r + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


print(gcd(x, y))
