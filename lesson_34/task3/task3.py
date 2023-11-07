import requests


class WeatherInfo:
    def __init__(self, json_data):
        self.temperature = json_data['main']['temp']
        self.wind_speed = json_data['wind']['speed']
        self.pressure = json_data['main']['pressure']
        self.humidity = json_data['main']['humidity']
        self.description = json_data['weather'][0]['description']

    def printInfo(self):
        print(f'Temperature : {self.temperature} degree celcius')
        print(f'Wind Speed : {self.wind_speed} m/s')
        print(f'Pressure : {self.pressure}')
        print(f'Humidity : {self.humidity}')
        print(f'Description : {self.description}\n')


print("-------> CONSOLE WEATHER APP <-------\n")
while True:
    city = input("Input a city:\n0 - exit\n")
    if city == '0':
        break
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b94a41d8dd0c853d193d5aa541aaf128&units=metric'
    if requests.get(url).ok:
        print(f"Wheather in {city.capitalize()}:")
        weather = WeatherInfo(requests.get(url).json())
        weather.printInfo()
    else:
        print("No such city. Try again")
