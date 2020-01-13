from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^Local/$', LocalList.as_view()),
    url(r'^Local/(?P<pk>[0-9]+)/$', LocalDetail.as_view()),
    url(r'^Raza/$', RazaList.as_view()),
    url(r'^Raza/(?P<pk>[0-9]+)/$', RazaDetail.as_view()),
    url(r'^TipoMascota/$', TipoMascotaList.as_view()),
    url(r'^TipoMascota/(?P<pk>[0-9]+)/$', TipoMascotaDetail.as_view()),
]