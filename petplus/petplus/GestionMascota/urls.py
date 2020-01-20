from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from .views import *
from django.conf.urls import handler404


urlpatterns = [
    url(r'^rol/$',RolList.as_view(), name ='rol'),
    url(r'^rol/(?P<pk>[0-9]+)/$', RolDetail.as_view()),

    url(r'^usuario/$', UsuarioList.as_view(), name='usuario'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', UsuarioDetail.as_view()),

    url(r'^raza/$',RazaList.as_view(), name ='raza'),
    url(r'^raza/(?P<pk>[0-9]+)/$', RazaDetail.as_view()),

    url(r'^tipomascota/$', TipoMascotaList.as_view(), name='tipomascota'),
    url(r'^tipomascota/(?P<pk>[0-9]+)/$', TipoMascotaDetail.as_view()),

    url(r'^mascota/$',MascotaList.as_view(), name ='mascota'),
    url(r'^mascota/(?P<pk>[0-9]+)/$', MascotaDetail.as_view()),

    url(r'^local/$', LocalList.as_view(), name='local'),
    url(r'^local/(?P<pk>[0-9]+)/$', LocalDetail.as_view()),

    url(r'^recomendar/$',RecomendarList.as_view(), name ='recomendar'),
    url(r'^recomendar/(?P<pk>[0-9]+)/$', RecomendarDetail.as_view()),

    url(r'^cuidado/$', CuidadoList.as_view(), name='cuidado'),
    url(r'^cuidado/(?P<pk>[0-9]+)/$', CuidadoDetail.as_view()),

    url(r'^planificacion/$',PlanificacionList.as_view(), name ='planificacion'),
    url(r'^planificacion/(?P<pk>[0-9]+)/$', PlanificacionDetail.as_view()),

]