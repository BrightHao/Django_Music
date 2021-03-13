import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
django.setup()

import requests
from bs4 import BeautifulSoup
from songslist.models import Songs, SongsList

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/67.0.3396.99 Safari/537.36"}


def get_music(Songlistid, id, tables):
    songslist_id = id
    url = 'https://music.163.com/playlist?id=' + str(songslist_id)
    insert_list = list()
    s = requests.session()
    s = BeautifulSoup(s.get(url, headers=header).content, 'lxml')

    id_list = s.select('ul.f-hide li a')

    #查詢歌單數據表
    joe = SongsList.objects.get(id=Songlistid)
    i = 1
    previous_songs_num = len(Songs.objects.all())
    for songs in id_list:
        name = songs.text
        id = songs.get('href')[9:]
        url = 'http://music.163.com/song/media/outer/url?id=' + id
        insert_list.append(tables(song_id=id, name=name, url=url))
        i += 1
    tables.objects.bulk_create(insert_list)
    print(f"成功创建{i}个数据表")
    SONGS = Songs.objects.all()[previous_songs_num:]
    for song in SONGS:
        song.songslist.add(joe)
    print(f"{tables}{Songlistid}数据更新完毕")

songslist = SongsList.objects.all()[39:]
for i in songslist:
    songslist_id = i.id
    list_id = i.list_id
    get_music(songslist_id, list_id, Songs)
