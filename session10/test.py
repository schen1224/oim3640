s='IPHONE'

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# To check the letter 'c' in s is lowercase or not


def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"


# 'flag' is rather True or False, it is used to test c in s


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


# It is pretty much the same as first one, becasue is c is lowercase, flag = False or True, it is True


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# It is doing the same thing


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
a="iPhone"
b='Babson'
c='python'
print(any_lowercase5(c))
# 221

