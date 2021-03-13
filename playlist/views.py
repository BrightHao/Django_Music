from django.shortcuts import render
from songsrank import models


# Create your views here.
#播放页面的视图函数
def douyin_songlist(request):
    songs = models.Douyin_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def popular_songlist(request):
    songs = models.Popular_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def hot_songlist(request):
    songs = models.Hot_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def new_songlist(request):
    songs = models.New_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def dianyin_songlist(request):
    songs = models.Dianyin_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def dianjing_songlist(request):
    songs = models.Dianjing_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def ktv_songlist(request):
    songs = models.KTV_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def BillBoard_songlist(request):
    songs = models.BillBoard_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def UK_songlist(request):
    songs = models.UK_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def Q_songlist(request):
    songs = models.Q_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

def Oricon_songlist(request):
    songs = models.Oricon_Song_Rank.objects.all()
    songid = request.GET.get('songid')
    if not songid:
        songid = 1
    kwgs = {
        "songs": songs,
        "songid": songid
    }
    return render(request, 'player.html', kwgs)

