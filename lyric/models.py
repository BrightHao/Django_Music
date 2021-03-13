from django.db import models


class Lyric(models.Model):
    songid = models.CharField("歌曲ID", primary_key=True, max_length=20)
    name = models.CharField("歌曲名", max_length=64)
    singer = models.CharField("歌手名", max_length=64)
    lyric = models.CharField("歌曲歌词", max_length=2048)

    class Meta:
        verbose_name_plural = "歌词"

    def __str__(self):
        return self.name
