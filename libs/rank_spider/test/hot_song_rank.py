import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")# project_name 项目名称
django.setup()

import requests
from bs4 import BeautifulSoup
from songsrank import models


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/67.0.3396.99 Safari/537.36"}


url = "https://music.163.com/discover/toplist?id=3778678"

#将歌曲名和id存入列表
def get_music():
    #定义一个列表，用于存放每首歌的简要信息
    # music_list = []
    #获得网页代码，进行解析
    html = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(html, 'lxml')

    # 将每首歌曲的信息全部存到id_list里面   这里的id_list不是一个列表，而是一个字符串类型
    id_list = soup.find('textarea').get_text()
    #这里将null和false变为字符串形式，为了避免将str转化为list的时候报错
    null = "null"
    false = "false"
    #将字符串转化为字典
    id_list = eval(id_list)

    #清空数据库
    models.Hot_Song_Rank.objects.all().delete()

    #i为每首歌的具体信息，是以字典格式呈现的
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
        info = { "id": id, "name": name, "singer": singer, "album": album, "pic_url": picurl, "sing_url": sing_url}
        data = models.Hot_Song_Rank.objects.create(**info)
        data.save()


get_music()
