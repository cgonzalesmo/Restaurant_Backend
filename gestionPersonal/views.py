from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from gestionPersonal.serializers import UsuarioSerializers
# Create your views here.

@api_view(['GET'])
def usuario_view(request):
    serializers = UsuarioSerializers(request.user)
    return Response(serializers.data)