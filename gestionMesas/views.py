from gestionMesas.models import G1_MESA

from django.shortcuts import render

from rest_framework import viewsets
from gestionMesas.serializers import MesaSerializer



# Create your views here.



class MesaViewset(viewsets.ModelViewSet):
    queryset = G1_MESA.objects.all()
    serializer_class = MesaSerializer
