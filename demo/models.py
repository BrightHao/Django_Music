from django.db import models



class Singers(models.Model):
    name = models.CharField("歌手", max_length=10)
    singerid = models.CharField("歌手id", max_length=24)

    class Meta:
        verbose_name_plural = "歌手"

    def __str__(self):
        return self.name


class Songs(models.Model):
    songid = models.CharField("歌曲id", max_length=24)
    name = models.CharField("歌曲名", max_length=64)
    singer = models.ForeignKey(Singers)
    song_url = models.CharField("歌曲链接", max_length=256)

    class Meta:
        verbose_name_plural = "歌曲"

    def __str__(self):
        return self.name


class Albums(models.Model):
    name = models.CharField("专辑", max_length=64)
    albumid = models.CharField("专辑id", max_length=32)
    singer = models.ForeignKey(Singers)
    song = models.ManyToManyField(Songs)
    # image = models.ImageField("专辑图片", upload_to="../static/imaages/album", null=True, blank=True)
    image = models.CharField("专辑图片地址", max_length=256)

    class Meta:
        verbose_name_plural = "专辑"

    def __str__(self):
        return self.name
