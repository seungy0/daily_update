import requests
from bs4 import BeautifulSoup

url = 'https://www.billboard.com/charts/hot-100'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    rank = soup.select('li > button > span.chart-element__rank.flex--column.flex--xy-center.flex--no-shrink > span.chart-element__rank__number')
    song = soup.select('li > button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary')
    singer = soup.select('li > button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary')
    music_chart = []
    for i in zip(rank, song, singer):
        music_chart.append({
            'rank': i[0].text,
            'song': i[1].text,
            'singer': i[2].text,
        })
    for i in music_chart:
        print(i)
else:
    print(response.status_code)
