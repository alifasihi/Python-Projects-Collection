# API Reference https://cutt.ly/
from typing import Final
import requests

API_KEY: Final[str] = 'e40ec1d77c0454ad42cf36eba6bfe344a952d'

BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_url(full_url: str):
    paload: dict = {'key': API_KEY, 'short': full_url, }
    requset = requests.get(BASE_URL, paload)
    data: dict = requset.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_url: str = url_data['shortLink']
            print('Url:', short_url)
        else:
            print('Error Status:', url_data['status'])


def main():
    url:str=input('Enter Url: >>')

    shorten_url(url)


if __name__ == '__main__':
    main()