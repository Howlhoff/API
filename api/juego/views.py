from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from rest_framework.generics import ListAPIView
from .models import *

# Create your views here.

class JuegoView(ListAPIView):
    serializer_class = JuegoSerializer
    def get_queryset(self):
        if self.request.method == 'GET':
            nombre = self.request.GET.get("id_buscador",None)
            if nombre is not None:
                return juego.objects.filter(nombre=nombre)
            return juego.objects.all()
