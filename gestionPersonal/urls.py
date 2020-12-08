from django.urls import path

from gestionPersonal import views



urlpatterns = [
    path('usuario/', views.usuario_view)
]
