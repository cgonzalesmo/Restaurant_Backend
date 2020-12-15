from django.urls import path , include

from gestionProductos import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('categoria', views.ProductoCategoriaViewset)
router.register('producto', views.ProductoViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]
