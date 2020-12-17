from django.urls import path , include

from gestionMesas import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('mesa', views.MesaViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]