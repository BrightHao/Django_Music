from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url(r'songslist_frame/$', views.recommend),
    url(r'songslist_frame/1$', views.recommend, name='recommend'),
    url(r'songslist_frame/3$', views.folksongs, name='folksongs'),
    url(r'songslist_frame/2$', views.popular, name='popular'),
    url(r'songslist_frame/4$', views.gufeng, name='gufeng'),

    url(r'listid=(?P<id>\d+)/$', views.listdetail),
]