# Exercise 1

prefixes = "JKLMNOPQ"
for letter in prefixes:
    if letter == "Q":
        suffix = "uack"
    elif letter == "O":
        suffix = "uack"
    else:
        suffix = "ack"
    print(letter + suffix)


# Exercise 2


def count(word):
    count = 0
    for letter in word:
        if letter == "a":
            count = count + 1
    return count


# Exercise 3


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


# Exercise 4

# To check is all letters in s are lowecase or not
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


# Exercise 5


def rotate_world(str, int):

    for letter in str:
        x = ord(letter) + int
        if x > 122:
            a = x - 123
            x = 97 + a
            print(chr(x))
        elif x < 97:
            a = 97 - x
            x = 123 - a
            print(chr(x))
        else:
            print(chr(x))

