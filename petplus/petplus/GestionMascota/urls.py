from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^Local/$', LocalList.as_view()),
    url(r'^Local/(?P<pk>[0-9]+)/$', LocalDetail.as_view()),
]