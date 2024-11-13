import urllib
import urllib.request
import urllib.parse
import json


class WeatherRetriever(object):
    def __init__(self):
        self.api_url = 'https://samples.openweathermap.org/data/2.5/\
weather?q={},{}&appid=439d4b804bc8187953eb36d2a8c26a02'

    # takes input (city and country), produces a URL string,
    # generate HTTP request, and returns the data.
    def fetch_weather_data(self, city, country):
        city = urllib.parse.quote(city)
        url = self.api_url.format(city, country)
        return urllib.request.urlopen(url).read()


class Crawler(object):
    def crawl_weather_data(self, weather_data):
        data = json.loads(weather_data)

        # fetch the current temperature
        temp_data = data['main']['temp']
        return temp_data


class Converter(object):
    """ converts the temperature from kelvin to celcius """

    def from_kelvin_to_celcius(self, kelvin):
        return kelvin - 273.15


class WeatherForecast(object):
    def __init__(self, data):
        self.temperature = data


class FacadeDesign(object):
    def get_forecast(self, city, country):
        weather_retriever = WeatherRetriever()
        weather_data = weather_retriever.fetch_weather_data(city, country)

        crawl = Crawler()
        crawl_data = crawl.crawl_weather_data(weather_data)
        weather = WeatherForecast(crawl_data)
        converter = Converter()
        temp_celcius = converter.from_kelvin_to_celcius(weather.temperature)
        return temp_celcius


if __name__ == '__main__':
    facadeDesign = FacadeDesign()
    print("So today's forecast is about ",
          facadeDesign.get_forecast('London', 'uk'), "degrees")
