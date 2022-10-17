# names = ['John', 'Paul', 'Goerge']
# scores = [95, 75, 85]
# grades = dict()
# print(grades)
# grades ={'John': 90, 'Paul': 75, 'Goerge': 85}
# print(grades)
# print(grades['Paul'])

# Exercise 1:
def histogram(word):
    dictionary = dict()
    for c in word:
        dictionary[c] = 1 + dictionary.get(c, 0)
    return dictionary

print (histogram('sabrina'))


'''
Exercise 3:
The global variable is number_fib_calls. The difference between this global variable and known is number_fib_calls is created inside a function but added with an attribute (global). Known is created outside the function without adding any attribute.
Also, I guess before adding global to number_fib_calls, number_fib_calls is a local variable. Whereas known is recognized by all functions?
'''


'''
Exercise 4:

Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.
'''

def create_word_dict():
    f = open('words.txt')
    word_dict = dict()
    for line in f:
        word = line.strip()
        word_dict[word] = word
    return word_dict


aList = ["sabrina","chen","sabrina"]

def has_duplicates(aList):
    dictionary =dict()
    for word in aList:
        dictionary[word] = 1 + dictionary.get(word, 0)
        if dictionary[word] > 1:
            return True
    return False



       







