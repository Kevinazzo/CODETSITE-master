from django.conf.urls import url
from . import views

#subURLS ex. productos/1
urlpatterns = [
    url(r'^$',views.home, name='home'),#productos/
    url(r'^(?P<subtipo_ID>[0-9]+)$', views.sublist, name='sublist')
]