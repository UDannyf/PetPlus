from .serializers import *
from .models import Local
from rest_framework import generics


class LocalList(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class RazaList(generics.ListCreateAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class RazaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer


class TipoMascotaList(generics.ListCreateAPIView):
    queryset = TipoMascota.objects.all()
    serializer_class = TipoMascotaSerializer

class TipoMascotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoMascota.objects.all()
    serializer_class = TipoMascotaSerializer