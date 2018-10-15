from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index1,name='index1'),
    url(r'^details_c/(?P<pk>\w{0,50})/$', views.details_c),
    url(r'^add_c', views.add_c, name='add_c'),
    url(r'^delete_c/(?P<pk>\w{0,50})/$',views.delete_c, name='delete_c'),
    ]
