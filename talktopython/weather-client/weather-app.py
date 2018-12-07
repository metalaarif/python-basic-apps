#!/usr/bin/python3
import requests
import bs4
import collections

def main():
    header()
    city = input("Enter the city you want to get weather for (london)? ")
    html = get_html_for_location(city)
    report = get_weather_from_html(html)
    print("The temperature in {} is {}{} and it is {}. ".format(report[0], report[1], report[2], report[3]))

def header():
    print("-" * 50)
    print("\t Realtime Weather Client App")
    print("-" * 50)

def get_html_for_location(name):
    url = "http://www.wunderground.com/weather-forecast/{}".format(name)
    response = requests.get(url)

    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(class_="row").find("h1").get_text()
    temp = soup.find(class_="current-temp").find(class_="wu-value wu-value-to").get_text()
    scale = soup.find(class_="current-temp").find(class_="wu-label").get_text()
    condition = soup.find(class_="condition-icon small-6 medium-12 columns").find("p").get_text()

    loc = cleanup_text(loc)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    condition = cleanup_text(condition)

    return loc, temp, scale, condition

def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text

if __name__ == '__main__':
    main()