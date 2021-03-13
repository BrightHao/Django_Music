from django.shortcuts import render
from . import models

# Create your views here.

#显示在排行榜详情页的视图函数
def detail1(request):
    songs = models.Popular_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail2(request):
    songs = models.New_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail3(request):
    songs = models.Hot_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail4(request):
    songs = models.Douyin_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail5(request):
    songs = models.Dianyin_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail6(request):
    songs = models.Dianjing_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail7(request):
    songs = models.KTV_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail8(request):
    songs = models.BillBoard_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail9(request):
    songs = models.UK_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail10(request):
    songs = models.Q_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)

def detail11(request):
    songs = models.Oricon_Song_Rank.objects.all()
    kwgs = {
        "songs": songs,
    }
    return render(request, 'SongsDetail.html', kwgs)
