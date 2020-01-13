from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    url('api/', include('petplus.GestionMascota.urls')),
    url(r'^admin/', admin.site.urls),
]