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

# Read the city names from txt file and put each city into a Python list
cities = []
with open("WS_cities.txt") as f:
	for line in f:
		cities.append(line.strip())
# Prints the Python list
print(cities)


# Loops through the cities
for city in cities:
	
	# Gets the weather data for each one
	parameters = {'access_key': API_KEY, 'query': city}
	response = requests.get(WS_URL, parameters)
	js = response.json()
	temperature = js['current']['temperature']
	date = js['location']['localtime']
	
	# Opens a file with the same name as each city and writes the date and temperature to each file, appending it to the existing data
	with open(f"WS_{city}.txt", "a") as f:
		f.write(f"{date},{temperature}\n")
