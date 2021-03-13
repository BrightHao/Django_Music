import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
django.setup()


from songsrank import models
from lyric import models as ly_models
import requests
import json
import threading


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/67.0.3396.99 Safari/537.36"}


def get_lyric(model):
    list = model.objects.all()
    for i in list:
        url = "http://music.163.com/api/song/lyric?id=" + i.id + "&lv=1&kv=1&tv=1"
        res = json.loads(requests.get(url, headers=header).text)
        if "lrc" not in res:
            continue
        lyric = res["lrc"]["lyric"]
        try:
            ly_models.Lyric.objects.create(songid=i.id, name=i.name, singer=i.singer, lyric=lyric)
            print(i.name + "歌词下载成功")
        except:
            print(i.name + "下载失败")

ll = [models.New_Song_Rank, models.Douyin_Song_Rank, models.Hot_Song_Rank, models.Popular_Song_Rank,
      models.Dianyin_Song_Rank, models.Dianjing_Song_Rank, models.KTV_Song_Rank, models.BillBoard_Song_Rank,
      models.UK_Song_Rank, models.Q_Song_Rank, models.Oricon_Song_Rank]

task_list = []
for i in ll:
    t = threading.Thread(target=get_lyric, args=(i, ))
    t.start()
    task_list.append(t)
[i.join() for i in task_list]

