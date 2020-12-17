from gestionComprobante.models import G2_COMPROBANTE
from gestionComprobante.models import GZZ_TIPO_PAGO

from django.shortcuts import render

from rest_framework import viewsets
from gestionComprobante.serializers import TipoPagoSerializer
from gestionComprobante.serializers import ComprobanteSerializer



# Create your views here.



class ComprobanteViewset(viewsets.ModelViewSet):
    queryset = G2_COMPROBANTE.objects.all()
    serializer_class = ComprobanteSerializer

class TipoPagoViewset(viewsets.ModelViewSet):
    queryset = GZZ_TIPO_PAGO.objects.all()
    serializer_class = TipoPagoSerializer