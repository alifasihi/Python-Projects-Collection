import requests
import bs4


def get_html(course_id: int) -> str:
    url = f'https://toplearn.com/c/{course_id}'

    response = requests.get(url)
    # print(response.status_code)
    return response.text


def get_title(html: str) -> str:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('.right-side h1')
    if not header:
        return 'there is no courses'
    else:
        return header.text.strip()


for course_id in range(6110,6159):
    html = get_html(course_id)
    title = get_title(html)
    print(title)
