"""
-------------------------------------------------------------------------------
Q1. (30 points) Please complete the function that uses your APIKEY to get
current wind speed in your hometown from openweathermap.org.
Notice: If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below, but
you will lose 10 points.
APIKEY = '8f62260aa7890d58d9a026e2810341ea'
If you use YOUR_OWN_APIKEY, please use it directly in the code. DO NOT import
it from a file that is ignored by Git.
-------------------------------------------------------------------------------
"""
import urllib.request
import json


def get_wind_speed(city, country):
    """
    Returns current wind speed in a given city from api.openweathermap.org
    """
    APIKEY = 'e998e60a5b1163b8d20392ab4093b237'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={APIKEY}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    wind=response_data.get('wind')
    for i in wind:
        wind.get('speed')
        result=wind.get('speed')
    return(result)


## When you've completed your function, uncomment the following lines and run this file to test!
# print(get_wind_speed('wellesley', 'us')) # you can replace the arguments with your hometown city and country code. If there are two (or more) words in the city name, you need to add '+' or '%20' between words, i.e. if you are from New York, try "new+york" or "new%20york".

## Expected output - of course the temperature in your hometown might be different:
# 4.8

"""
----------------------------------------------------------------------
Q2. (25 points) Given a string, replace vowels in the string with 
numbers based on the following rules and return the new string. Please 
complete the function. 
Notice: if you use more than one `if`, you will lose 10 points.
Rules:
vowel   ->  number
    a   ->  4
    e   ->  3
    i   ->  1
    o   ->  0
    u   ->  7
----------------------------------------------------------------------
"""


def encrypt(text):
    """
    Given a string, replace vowels in the string with numbers based on rules
    defined above, and return the new string
    """

    b = text
    y = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    new_list = ['4', '3', '1', '0', '7']
    for x in vowels_list:
        for y in range(len(text)):
            if x == text[y]:
                a = new_list[vowels_list.index(x)]
                b = b.replace(x,a)
                y = y +1
    return b

## When you've completed your function, uncomment the following lines and run this file to test!
# s1 = "babson college"
# s2 = "how are you?"
# print(encrypt(s1))
# print(encrypt(s2))

## Expected output:
## b4bs0n c0ll3g3
## h0w 4r3 y07?


"""
-------------------------------------------------------------------------------
Q3. (20 points) There are 351 towns/cities in Massachusetts. One of OIM-APIs 
(https://oim-apis.herokuapp.com/mass) returns JSON data of all town names 
(and other information). Please complete the function that returns the town name
 list. This list should be sorted alphabetically.
Notice: for Q3-Q5, you may create additional helper function(s) if needed. If you 
create additional function(s), you may change the given function(s) by adding 
necessary parameter(s).
-------------------------------------------------------------------------------
"""


def get_town_names():
    """
    Returns a sorted list of town names
    """
    town=[]
    url = f'https://oim-apis.herokuapp.com/mass'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    for name in response_data:
        town = name.strip()
        town.append(name)
    return sorted(town)


## When you've completed your function, uncomment the following lines and run this file to test!
names = get_town_names()
print(type(names), len(names))
print(names)

## Expected output:
# <class 'list'> 351
# ['Abington', 'Acton', 'Acushnet', 'Adams', 'Agawam', 'Alford', 'Amesbury', 'Amherst', ..., 'Yarmouth']


"""
-------------------------------------------------------------------------------
Q4. (15 points) You may have noticed you are the mayor of one or several towns 
in Massachusetts. Please complete the function that returns a dictionary - in 
this dictionary, key is mayor's name and value is a list of town names that the
mayor is managing. You can find example from the expected output below.
-------------------------------------------------------------------------------
"""


# def get_mayor_dict():
#     """
#     Returns a dictionary that maps mayors to their towns, {str: list}
#     """
#     d = {}
#     url = f'https://oim-apis.herokuapp.com/mass'
#     f = urllib.request.urlopen(url)
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     for line in response_data:
#         word = line.strip()
#         d[word] = 1
#     return d

def get_mayor_dict():
    url = f'https://oim-apis.herokuapp.com/mass'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    lst=list(response_data)
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    n=res_dct.get('name')
    m=res_dct.get('major')
    return (n,m)


## When you've completed your function, uncomment the following lines and run this file to test!
# mayor_dict = get_mayor_dict()
# print(mayor_dict['Jean']) # you can replace 'Jean' with your name

## Expected output - it is ok if the order is different:
# ['Bernardston', 'Hopkinton', 'Lee', 'Mansfield', 'Northampton', 'Shirley', 'Sterling', 'Williamsburg']


"""
-------------------------------------------------------------------------------
Q5. (10 points) Have you wondered how many people you are managing? Please 
complete the function that returns a list of all the mayor names sorted by 
the total population they are managing from most to least. You can find example 
from the expected output below.
-------------------------------------------------------------------------------
"""


def sort_mayors():
    """
    Returs a list that shows the mayor names sorted by the total population
    they are managing from most to least.
    """
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}
    sorted_dict.append(sorted_values[i])
    for i in sorted_dict:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
    return sorted_dict


# sorted_mayor_list = sort_mayors()
# print(sorted_mayor_list) # Callum is the busiest mayor because he manages almost 1 million people

# Expected output:
# ['Callum', 'Steven', 'Shinichi', 'Jiaxi', 'Jose', 'Ana', 'Peter', 'Tatsumi', 'Danny', 'Kaitlyn', 'Siyang', 'Benji', 'Ziqi', 'Tom', 'Mads', 'Ryan', 'Leo', 'Hrishi', 'Maria', 'Jared', 'Ross', 'Pratik', 'Yucheng', 'Luiz', 'Robin', 'Hanlu', 'Haoyang', 'Alex', 'Asa', 'Bruno', 'Jiaying', 'Zhixuan', 'Jean', 'Sakshyam', 'Tyler', 'Peiyu', 'Wilson', 'Matthew', 'Thomas', 'Siqi', 'Lucy', 'Hongchen']
