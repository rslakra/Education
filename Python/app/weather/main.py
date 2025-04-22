# Author: Rohtash Lakra
import requests
import urllib.parse as urlparse
import json

# Installation Instructions
# python3 -m venv path/to/venv
# brew install python-requests
# python3 -m pip install requests
# 


# Generic Urls
# 
# url = "https://openweathermap.org/data/2.5/onecall?lat=37.6688&lon=-122.0808&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"
# base_url = "https://openweathermap.org/data/2.5/onecall"
# https://openweathermap.org/data/2.5/weather?lat=37.6688&lon=-122.0808&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02
# 

# 
# https://openweathermap.org/api/one-call-3
# 
# 
# App Class
class App:
    api_key = "439d4b804bc8187953eb36d2a8c26a02"
    content_type = "Content-Type"
    content_type_value = "application/json; charset=utf-8"
    base_url = "https://openweathermap.org/api/one-call-3"

    # __init__
    def __init__(self):
        self.params = {}


    # sets the base_url
    def set_base_url(self, base_url):
        self.base_url = base_url


    # Builds the request url with param
    def build_request_url(base_url, params):
        if len(params) > 0:
            return "?".join([base_url, urlparse.urlencode(params)])
        else:
            return base_url


# Params Class
class HttpQueryBuilder:

    # __init__
    def __init__(self):
        self.params = {}
        print(f"{self.params}")

    # add params
    def add_param(self, key, value):
        self.params[key] = value
        print(f"{self.param}")

    # Builds the request url with param
    def build_request__url(self, base_url):
        return App.build_request_url(base_url, self.params)


# City Class
class City:

    base_url = "https://openweathermap.org/data/2.5/weather"

    # Constructor
    def __init__(self, name, latitude, longitude, units = "metric"):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        self.unit_symbol = "C"
        # update the unit-symbol based on units
        if self.units != "metric":
            self.unit_symbol = "F"

        self.json_response = {}

    def __str__(self) -> str:
        return f"{self.name} <units={self.units}, latitude={self.latitude}, longitude={self.longitude}>"
    

    # Get's the weather info of this city
    def get_weather_data(self):
        # set params
        params = {}
        params["appid"] = App.api_key
        params["units"] = self.units
        params["lat"] = self.latitude
        params["lon"] = self.longitude

        # base_url = "https://openweathermap.org/data/2.5/weather"

        # build request
        url = App.build_request_url(City.base_url, params)

        self.json_data = {}
        # Send api request
        try:
            print(f"Url: {url}")
            response = requests.get(url)
            # headers = response.headers
            # cookies = response.cookies
            # content = response.content
            print(f"Response: {response.status_code}")
            self.json_response = response.json();
            # print(json_data)
        except Exception as ex:
            print(f"{ex}")
            self.json_response["error"] = ex

        # extra data from json
        self.city = self.json_response["name"]
        self.country = self.json_response["sys"]["country"]

        self.weather = self.json_response["weather"]
        self.weather_main = self.weather[0]["main"]
        self.weather_description = self.weather[0]["description"]

        self.weather_data = self.json_response["main"]
        self.temp = self.weather_data["temp"]
        self.min_temp = self.weather_data["temp_min"]
        self.max_temp = self.weather_data["temp_max"]
        self.pressure = self.weather_data["pressure"]
        self.humidity = self.weather_data["humidity"]

        self.wind_speed = self.json_response["wind"]["speed"]
        self.clouds = self.json_response["clouds"]["all"]

    def log_response_data(self):
        print(f"Response: {self.json_response}")


    # Prints weather details
    def print_weather_details(self):
        print("\n")
        # Hayward (Clouds - overcast clouds)
        print(f'{self.city}, {self.country} ({self.weather_main} - {self.weather_description})')
        # 2.7°С temperature from 12.7 to 15.9 °С, wind 4.12 m/s. clouds 100 %, 1017 hpa
        print(f'{self.temp}°{self.unit_symbol} temperature from {self.min_temp} to {self.max_temp} °{self.unit_symbol}, wind {self.wind_speed} m/s. clouds {self.clouds} %, {self.pressure} hpa, {self.humidity} % humidity')
        print("\n")


# Hayward Temperature Info
city = City("Hayward", 37.6688, -122.0808)    
print(city)
city.get_weather_data()
city.print_weather_details()
# city.log_response_data()


# Rohtak Temperatuire Info
city = City("Rohtak", 28.895515, 76.606613, "imperial")
print(city)
city.get_weather_data()
city.print_weather_details()
# city.log_response_data()
