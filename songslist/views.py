from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Songslist_index.html')


def recommend(request):
    from songslist.models import SongsList
    songslist = SongsList.objects.filter(Class='推荐')[:6]
    current_name = "recommend"
    kwgs = {
        'songslists': songslist,
        'current_name': current_name,
    }
    return render(request, 'songslist_frame.html', kwgs)

def popular(request):
    from songslist.models import SongsList
    songslist = SongsList.objects.filter(Class='流行')[:6]
    current_name = "popular"
    kwgs = {
        'songslists': songslist,
        'current_name': current_name,
    }
    return render(request, 'songslist_frame.html', kwgs)

def folksongs(request):
    from songslist.models import SongsList
    songslist = SongsList.objects.filter(Class='民谣')[:6]
    current_name = "folksongs"
    kwgs = {
        'songslists': songslist,
        'current_name': current_name,
    }
    return render(request, 'songslist_frame.html', kwgs)

def gufeng(request):
    from songslist.models import SongsList
    songslist = SongsList.objects.filter(Class='古风')[:6]
    current_name = "gufeng"
    kwgs = {
        'songslists': songslist,
        'current_name': current_name,
    }
    return render(request, 'songslist_frame.html', kwgs)



def listdetail(request, id):
    from songslist.models import Songs, SongsList
    List = SongsList.objects.get(id=id)
    List.listen_times += 1
    List.save()
    songs_query = Songs.objects.filter(songslist=List)
    kwgs = {
        'songs': songs_query,
        'list': List,
        'songs_num': len(songs_query),
    }
    return render(request, 'Songslist_detail.html', kwgs)
