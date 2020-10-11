#! python3
# getOpenWeather.py - From the command line, prints out the current weather in a location

import json, requests, sys

APPID = 'YOUR APP ID AS A STRING' # Get your API key from https://openweathermap.org

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code OR 2-letter_state_abbreviation')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's Current Weather Data API
url = 'https://api.openweathermap.org/data/2.5/weather?q={},&units=imperial&appid={}'.format(location, APPID)

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

print('Current weather in {}'.format(location))
print('Temperature: {}'.format(weatherData['main']['temp']) + ' degrees Fahrenheit')
print('Description: {}'.format(weatherData['weather'][0]['description']).title())
