import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
django.setup()

import requests
from bs4 import BeautifulSoup
from songsrank import models
import threading
import json

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/67.0.3396.99 Safari/537.36"}


def get_music(url, table):
    html = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(html, 'lxml')
    id_list = soup.find('textarea').get_text()
    id_list = json.loads(id_list)

    table.objects.all().delete()

    insert_list = list()
    for song in id_list:
        singer = ""
        if len(song["artists"]) != 1:
            for singer_info in song["artists"]:
                singer = singer + "/" + singer_info["name"]
            singer = singer[1:]
        else:
            singer = song["artists"][0]["name"]
        name = song["name"]
        id = song["id"]
        sing_url = f"http://music.163.com/song/media/outer/url?id={id}.mp3"
        album = song["album"]["name"]
        picurl = song["album"]["picUrl"]
        duration = song['duration']
        sec = duration/1000
        m, s = divmod(sec, 60)
        duration = ("%d:%02d" % (m, s))
        # info = {"id": id, "name": name, "singer": singer, "album": album, "pic_url": picurl, "sing_url": sing_url}
        # data = table.create(**info)
        # data.save()
        insert_list.append(table(id=id, name=name, singer=singer, album=album, pic_url=picurl, sing_url=sing_url, duration=duration))
    table.objects.bulk_create(insert_list)
    print(f"{table}数据更新完毕")

t1 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=3779629", models.New_Song_Rank))
t2 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=2250011882", models.Douyin_Song_Rank))
t3 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=3778678", models.Hot_Song_Rank))
t4 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=19723756", models.Popular_Song_Rank))
t5 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=1978921795", models.Dianyin_Song_Rank))
t6 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=2006508653", models.Dianjing_Song_Rank))
t7 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=21845217", models.KTV_Song_Rank))
t8 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=60198", models.BillBoard_Song_Rank))
t9 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=180106", models.UK_Song_Rank))
t10 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=2023401535", models.Q_Song_Rank))
t11 = threading.Thread(target=get_music, args=("https://music.163.com/discover/toplist?id=60131", models.Oricon_Song_Rank))
task_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]
for i in task_list:
    i.start()
[i.join() for i in task_list]

