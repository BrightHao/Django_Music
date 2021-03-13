import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
django.setup()

import time
import requests
from lxml import etree
from bs4 import BeautifulSoup
from songsrank.models import New_Song_Rank, Douyin_Song_Rank, Hot_Song_Rank, Popular_Song_Rank


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/67.0.3396.99 Safari/537.36"}



def get_music(url, table):
    html = requests.get(url=url, header=header).text
    soup = BeautifulSoup(html, 'lxml')
    id_list = soup.find('textarea').get_text()
    print(id_list)
    null = "null"
    false = "false"
    id_list = eval(id_list)


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
        # info = {"id": id, "name": name, "singer": singer, "album": album, "pic_url": picurl, "sing_url": sing_url}
        # data = table.create(**info)
        # data.save()
        insert_list.append(table(id=id, name=name, singer=singer, album=album, pic_url=picurl, sing_url=sing_url))
    table.objects.bulk_create(insert_list)
    print(f"{table}数据更新完毕")


get_music("https://music.163.com/discover/toplist?id=3779629", New_Song_Rank)
get_music("https://music.163.com/discover/toplist?id=2250011882", Douyin_Song_Rank)
get_music("https://music.163.com/discover/toplist?id=3778678", Hot_Song_Rank)
get_music("https://music.163.com/discover/toplist?id=19723756", Popular_Song_Rank)
