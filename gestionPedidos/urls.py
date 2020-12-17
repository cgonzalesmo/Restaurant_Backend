from django.urls import path , include

from gestionPedidos import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('comanda', views.ComandaViewset)
router.register('estadoPedido', views.EstadoPedidoViewset)
router.register('comandaProducto', views.ComandaProductoViewset)


urlpatterns = [
    path('api/', include(router.urls)),
]