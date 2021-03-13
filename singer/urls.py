from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.singer_index, name='index'),
    url(r'^id=(?P<id>\d+)&charnum=(?P<initial>\d+)/$', views.singer_spider),
    url(r'^singerid=(?P<id>\d+)&singer=(?P<name>(.*?))/$', views.singer_detail),
]
