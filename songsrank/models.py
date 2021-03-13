from django.db import models

# Create your models here.

class Popular_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)

    class Meta:
        verbose_name_plural = "流行歌排行榜"

    def __str__(self):
        return self.name


class Hot_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "热歌排行榜"

    def __str__(self):
        return self.name



class New_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "新歌排行榜"

    def __str__(self):
        return self.name


class Douyin_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "抖音排行榜"

    def __str__(self):
        return self.name

class Dianyin_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "电音排行榜"

    def __str__(self):
        return self.name

class Dianjing_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "电竞音乐榜"

    def __str__(self):
        return self.name

class KTV_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "KTV唛榜"

    def __str__(self):
        return self.name

class BillBoard_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "美国BillBoard榜"

    def __str__(self):
        return self.name

class UK_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "UK排行榜周榜"

    def __str__(self):
        return self.name

class Q_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "英国Q杂志中文版周榜"

    def __str__(self):
        return self.name

class Oricon_Song_Rank(models.Model):
    id = models.CharField("歌曲id", max_length=24, primary_key=True)
    name = models.CharField("歌名", max_length=64)
    singer = models.CharField("歌手", max_length=10)
    album = models.CharField("专辑", max_length=32)
    pic_url = models.CharField("歌曲专辑图片", max_length=256)
    sing_url = models.CharField("歌曲链接", max_length=256)
    duration = models.CharField("歌曲长度", max_length=32)


    class Meta:
        verbose_name_plural = "日本Oricon周榜"

    def __str__(self):
        return self.name