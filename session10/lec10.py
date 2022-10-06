# last one= length-1 because starts with 0
def duckings():
    prefixes='JKLMNOPQ'
    suffix='ack'
    for letter in prefixes:
        if letter=='o' or letter== 'Q':
            print(letter+'u'+suffix)
        else:
            print(letter+suffix)

print(duckings())
# index ('a') give you the position of the letter
# find gives you negative value if no result found
