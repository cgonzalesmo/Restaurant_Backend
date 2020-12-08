from gestionPersonal.models import G1_USUARIO
from rest_framework import serializers




class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = G1_USUARIO
        fields = '__all__'