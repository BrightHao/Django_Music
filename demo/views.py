from django.shortcuts import render, HttpResponse
from songsrank import models
from songslist.models import SongsList


def index(request):
    newsongs = models.New_Song_Rank.objects.all()[0:5]
    hotsongs = models.Hot_Song_Rank.objects.all()[0:5]
    popularsongs = models.Popular_Song_Rank.objects.all()[0:5]
    dianyinsongs = models.Dianyin_Song_Rank.objects.all()[0:5]
    lists = SongsList.objects.filter(Class="推荐")[:12]
    kwgs = {
        "newsong": newsongs,
        "hotsong": hotsongs,
        "popularsong": popularsongs,
        "dianyinsong": dianyinsongs,
        "lists": lists,
    }
    return render(request, 'base.html', kwgs)


def research(request, text):
    from demo.models import Songs
    songs = Songs.objects.filter(name=text).all()[:12]
    if len(songs) != 0:
        kwgs = {
            "songs": songs,
        }
        return render(request, "research_text.html", kwgs)
    else:
        return render(request, "Noresult.html")



