#!/usr/bin/python3
import requests
import bs4

def main():
    header()
    city = input("Enter the city you want to get weather for (london)? ")
    html = get_html_data(city)
    get_weather_from_html(html)

def header():
    print("-" * 50)
    print("\t Realtime Weather Client App")
    print("-" * 50)

def get_html_data(name):
    url = "http://www.wunderground.com/weather-forecast/{}".format(name)
    response = requests.get(url)

    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    print(soup)
if __name__ == '__main__':
    main()