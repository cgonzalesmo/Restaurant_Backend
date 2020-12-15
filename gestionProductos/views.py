from gestionProductos.models import G1_PRODUCTO
from gestionProductos.models import GZZ_PRODUCTO_CATEGORIA

from django.shortcuts import render

from rest_framework import viewsets
from gestionProductos.serializers import ProductoCategoriaSerializer
from gestionProductos.serializers import ProductoSerializer



# Create your views here.



class ProductoViewset(viewsets.ModelViewSet):
    queryset = G1_PRODUCTO.objects.all()
    serializer_class = ProductoSerializer

class ProductoCategoriaViewset(viewsets.ModelViewSet):
    queryset = GZZ_PRODUCTO_CATEGORIA.objects.all()
    serializer_class = ProductoCategoriaSerializer