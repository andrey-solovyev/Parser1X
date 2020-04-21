import requests
from bs4 import BeautifulSoup as BS

max_page = 4
pages = []

for x in range(1, max_page + 1):
    pages.append(requests.get('https://1x-bet78391.world/ru/live/Baccarat/' + str(x)))

for r in pages:
    html = BS(r.content, 'html.parser')

    for el in html.select('.lent-block'):
        title = el.select('.lent-title > a')
        print(title[0].text)
