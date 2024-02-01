# Testing API with WeatherStack

# Importing environmental variables
import os

# External library "requests" is for fetching data over the internet - this module (not actually part of Python)
import requests

# Local ReplIt: hiding my WeatherStack API key
my_secret = os.environ['APIkeyWeatherStack']

# Defining access arameters
API_KEY = my_secret
WS_URL = "http://api.weatherstack.com/current"
city = "Belgrade"
accessParameters = {'access_key': API_KEY, 'query': city}

response = requests.get(WS_URL, accessParameters)
js = response.json()

# Printing out raw JSON data
print(js)
print()

# Printing out formatted data
temperature = js['current']['temperature']
date = js['location']['localtime']
city = js['location']['name']
country = js['location']['country']
feelsLike = js['current']['feelslike']
print(
    f"The temperature in {city}, {country} on {date} is {temperature} degrees Celsius, which feels like {feelsLike} degrees Celsius"
)
