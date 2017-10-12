from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getSongs', views.getSongs, name='getSongs'),
    url(r'^get_singer_list', views.get_singer_list, name='get_singer_list'),
    url(r'^singer_list',views.singer_list,name='singer_list'),
    url(r'^get_singer_data', views.get_singer_data, name='get_singer_data'),
    url(r'^singer_info/(?P<singer_id>[0-9]+)/$',views.singer_info,name='singer_info'),
    url(r'^home',views.home,name='home'),
    url(r'^$',views.index,name='index'),
]
