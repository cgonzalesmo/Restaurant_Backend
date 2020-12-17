from gestionComprobante.models import G2_COMPROBANTE
from gestionComprobante.models import GZZ_TIPO_PAGO
from rest_framework import serializers


class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GZZ_TIPO_PAGO
        fields = '__all__'


        
class  ComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = G2_COMPROBANTE
        fields = '__all__'