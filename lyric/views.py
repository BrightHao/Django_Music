# from django.shortcuts import render
from django.http import HttpResponse
from . import models


def get(request):
    if request.method == "POST":
        id = request.POST.get('sid', None)
        try:
            text = models.Lyric.objects.get(songid=id).lyric
        except:
            text = "[00:00]该音乐暂无歌词"
        return HttpResponse(text, charset='utf-8')
    else:
        return HttpResponse("请求方式错误", charset='utf-8')
