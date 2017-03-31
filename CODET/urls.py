from django.conf.urls import url, include
from . import views

from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^productos/',include('products.urls')),
    url(r'^contacto/',views.contacto),
    url(r'^fabricaciones/',views.fabricaciones),
    url(r'^planta/',views.planta)
]
