import urllib.request
import json

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text) # j is a dictionary
    #print(j) 

# Can you print number of people in the space?
# x = j['people']
# print(len(x))
print(j.get('number',0))
print(j['number'])
# Can you print all the names?
x = j['people']
for i in x:
    name=i['name']
    craft=i['craft']
    print(name,craft)
    # print(j['people'][int(i)]['name']) #name is the key



 


