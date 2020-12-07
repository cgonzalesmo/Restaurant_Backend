from django.db import models
from gestionPedidos.models import G4_COMANDA
from gestionPersonal.models import G1_USUARIO

# Create your models here.
class GZZ_TIPO_PAGO(models.Model):
    TipPagCod = models.AutoField(verbose_name="Codigo de Categoria:", primary_key=True)
    TipPagNom = models.CharField(verbose_name="Nombre de Categoria:", max_length=20)

class G2_COMPROBANTE(models.Model):
    ComCod = models.AutoField(verbose_name="Codigo de Comprobante:", primary_key=True)
    ComCmdCod = models.ForeignKey(G4_COMANDA, on_delete=models.CASCADE)
    ComUsuCod = models.ForeignKey(G1_USUARIO, on_delete=models.CASCADE)
    ComTipPagCod = models.ForeignKey(GZZ_TIPO_PAGO, on_delete=models.CASCADE)
    ComTotVen = models.FloatField(verbose_name="Total de venta:")
    ComSubTotVen = models.FloatField(verbose_name="Subtotal de venta:")
    ComImpTotVen = models.FloatField(verbose_name="Impuesto de venta:")
    ComEfePag = models.FloatField(verbose_name="Pago Efectivo:")
    ComTarPag = models.FloatField(verbose_name="Pago Tarjeta:")
    ComCliNom = models.CharField(verbose_name="Nombre de Cliente:", max_length=50)
    ComCliDoc = models.CharField(verbose_name="Dni de Cliente:", max_length=8)
    ComCliDir = models.CharField(verbose_name="Direccion de Cliente:", max_length=70)
    ComFecEmi = models.DateTimeField(verbose_name="Fecha de Emision:")
    ComCan = models.BooleanField(verbose_name= "Comprobante Candelado:")
