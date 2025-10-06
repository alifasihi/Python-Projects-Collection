from bs4 import BeautifulSoup
import requests


def get_soup():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
    }

    request = requests.get('https://www.bbc.com/news', headers=headers)
    html = request.content

    soup = BeautifulSoup(html, features='html.parser')
    return soup


def get_headlines(soup):
    headlines = set()
    for h in soup.find_all('h2', class_="sc-9d830f2a-3 eHyegN"):
        headline = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)


def check_hesdline(headlines, term):
    term_list = []
    term_found = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            term_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <-----------------------------"{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('----------------------------------------------------')

    if term_found:
        print(f'"{term}" was mentioned {term_found} times.')
        print('----------------------------------------------------')

        for i, headline in enumerate(term_list, start=1):
            print(f'{i}: {headline.capitalize()}')
    else:
        print(f'no matches found for : "{term}"')
        print('----------------------------------------------------')


def main():
    soup = get_soup()
    headlines = get_headlines(soup=soup)

    user_input = input('Enter headlines to check: >>')
    check_hesdline(headlines, user_input)


if __name__ == '__main__':
    main()
