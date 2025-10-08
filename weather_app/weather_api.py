import json
import requests
from typing import Final
from model import Weather, dt

API_KEY: Final[str] = 'e976c5abdadde2ececee8c0490c600e9'
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city_name: str, mock: bool = False) -> dict:
    if mock:
        print('using mock date...')
        with open('dummy_date.json') as file:
            return json.load(file)

    payload: dict = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url=BASE_URL, params=payload)
    print(request.status_code)
    data: dict = request.json()

    with open('dummy_date.json', 'w') as file:
        json.dump(data, file)
    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')
    if not days:
        raise Exception(f'problem With json: {weather}')

    list_of_weather: list[Weather] = []

    for day in days:
        w: Weather = Weather(
            date=dt.fromtimestamp(day.get('dt')),
            details=(details := day.get('main')),
            temp=details.get('temp'),
            weather=(weather := day.get('weather')),
            description=weather[0].get('description'),

        )
        list_of_weather.append(w)
        return list_of_weather
