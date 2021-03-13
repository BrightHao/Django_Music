from django.conf.urls import url
from songsrank import views

urlpatterns = [
    url(r'^$', views.detail1, name='index'),
    url(r'^1/$', views.detail1, name='1'),
    url(r'^2/$', views.detail2, name='2'),
    url(r'^3/$', views.detail3, name='3'),
    url(r'^4/$', views.detail4, name='4'),
    url(r'^5/$', views.detail5, name='5'),
    url(r'^6/$', views.detail6, name='6'),
    url(r'^7/$', views.detail7, name='7'),
    url(r'^8/$', views.detail8, name='8'),
    url(r'^9/$', views.detail9, name='9'),
    url(r'^10/$', views.detail10, name='10'),
    url(r'^11/$', views.detail11, name='11'),
]