#################################################################
# 빌보드 차트 크롤링 해와서 mysql db에 삽입하고 데이터프레임 형태로 출력 #
#################################################################

import requests  # url로 사이트 코드 받아오는데 필요한 모듈
from bs4 import BeautifulSoup  # 크롤링을 위한 모듈
import pymysql  # python에서 mysql 쓰려면 필요한 모듈
import pandas as pd  # dataframe으로 깔끔하게 출력하려고 import
# 차트 크롤링
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
# mysql에 삽입
con = pymysql.connect(host='Localhost', user='user', password='0000', db='bilchart', charset='utf8')
cur = con.cursor(pymysql.cursors.DictCursor)
for i in music_chart:
    # print("%d %s %s" % (int(i['rank']), i['song'], i['singer']))
    i['song'] = i['song'].replace("'", "''")
    i['singer'] = i['singer'].replace("'", "''")
    sql = "INSERT IGNORE INTO bilchart (rank,song,singer) VALUES (%d,'%s','%s');" % (int(i['rank']), i['song'], i['singer'])
    cur.execute(sql)
    con.commit()

sql = "SELECT * from bilchart"
cur.execute(sql)
result = cur.fetchall()
result = pd.DataFrame(result)
print(result)
