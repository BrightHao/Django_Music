from django.db import models

# Create your models here.
class SongsList(models.Model):
    name = models.CharField("歌单名", max_length=64)
    list_id = models.CharField("歌单id", max_length=24)
    pic = models.CharField("歌单图片链接", max_length=256)
    date = models.DateField("歌单创建日期", auto_now=True)
    Class = models.CharField("歌单类型", max_length=32)
    listen_times = models.IntegerField("播放量")

    class Meta:
        verbose_name_plural = "歌单"

    def __str__(self):
        return self.name

class Songs(models.Model):
    song_id = models.CharField("歌曲id", max_length=32)
    name = models.CharField("歌曲名", max_length=64)
    url = models.CharField("歌曲资源URL", max_length=256)
    songslist = models.ManyToManyField(SongsList)

    class Meta:
        verbose_name_plural = "歌单歌曲"

    def __str__(self):
        return self.name
