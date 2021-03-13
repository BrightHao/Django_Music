from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.popular_songlist, name='SonglistIndex'),
    url(r'^1/$', views.popular_songlist, name='popular'),
    url(r'^2/$', views.hot_songlist, name='hot'),
    url(r'^3/$',views.new_songlist, name='new'),
    url(r'^4/$', views.douyin_songlist, name='douyin'),
    url(r'^5/$', views.dianyin_songlist, name='dianyin'),
    url(r'^6/$', views.dianjing_songlist, name='dianjing'),
    url(r'^7/$', views.ktv_songlist, name='ktv'),
    url(r'^8/$', views.BillBoard_songlist, name='BillBoard'),
    url(r'^9/$', views.UK_songlist, name='UK'),
    url(r'^10/$', views.Q_songlist, name='Q'),
    url(r'^11/$', views.Oricon_songlist, name='Oricon'),
    # url(r'^singer(?P<id>/d+)/$', ),
]