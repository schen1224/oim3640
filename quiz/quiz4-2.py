"""
-------------------------------------------------------------------------------
Q6. There are 351 towns/cities in Massachusetts. One of OIM-APIs 
(https://oim-apis.herokuapp.com/mass) returns JSON data of all town names 
(and other information). 

Please complete the function that returns a dictionary - in this dictionary, 

key is a letter and value is a list of town names that start with that letter.

Notice: you may create additional helper function(s) if needed. If you 
create additional function(s), you may change the given function(s) by adding 
necessary parameter(s).
-------------------------------------------------------------------------------
"""
from cgitb import reset
import string
import urllib.request
import json
import pprint

def first_letters():
    """
    Return: a dict that maps letter to towns, {str: list}
    """
    url = f'https://oim-apis.herokuapp.com/mass'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)
    map={}
    town=[]
    d=[]
    for d in response_data:
        town.append(d(str['name']))
        for letter in town:
            if letter[0] not in map:
                map[letter[0]] = set()
            map[letter[0]].add(letter)
    for key in map:
        map[key] = list(map[key])
    return map

# When you've completed your function, uncomment the
# following lines and run this file to test!
print(first_letters())


"""
--------------------------------------------------------------------------
Q7. Write a function that prints the dictionary from Q6. 

Your function should first print the longest list of towns with same first 
letter, followed by the second longest, and so on. 
--------------------------------------------------------------------------
"""

