from .serializers import LocalSerializer
from .models import Local
from rest_framework import generics


class LocalList(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer