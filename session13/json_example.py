import urllib.request
import json

APIKEY = 'e998e60a5b1163b8d20392ab4093b237'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?

tem=response_data.get('temp',287.23)
print(tem)