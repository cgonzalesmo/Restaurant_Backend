from gestionMesas.models import G1_MESA
from rest_framework import serializers

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = G1_MESA
        fields = '__all__'
