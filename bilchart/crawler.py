import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd

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
    # for i in music_chart:
    #     print(i)
else:
    print(response.status_code)

con = pymysql.connect(host='localhost', user='root', password='0000', db='bilchart', charset='utf8')
cur = con.cursor(pymysql.cursors.DictCursor)
for i in music_chart:
    sql = "INSERT INTO bilchart (rank,song,singer VALUE (%d,%s,%s))" % (int(i['rank']),i['song'],i['singer'])
    cur.execute(sql)
    con.commit()
sql = "SELECT * from bilchart"
cur.execute(sql)
result = cur.fetchall()
result = pd.DataFrame(result)
result
