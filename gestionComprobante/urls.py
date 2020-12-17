from django.urls import path , include

from gestionComprobante import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipoPago', views.TipoPagoViewset)
router.register('comprobante', views.ComprobanteViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]