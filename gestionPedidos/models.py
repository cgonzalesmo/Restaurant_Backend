from django.db import models
from gestionProductos.models import G1_PRODUCTO
from gestionMesas.models import G1_MESA
from gestionPersonal.models import G1_USUARIO
# Create your models here.

class G4_COMANDA(models.Model):
    CmdCod = models.AutoField(verbose_name="Codigo de Comanda:", primary_key=True)
    CmdHorEnt = models.DateTimeField(verbose_name="Hora Entrante de Comanda:")
    CmdHorSal = models.DateTimeField(verbose_name="Hora Salida de Comanda")
    CmdLle = models.BooleanField(verbose_name= "Llevar si/no:")
    CmdUsuCod = models.ForeignKey(G1_USUARIO, on_delete=models.CASCADE)
    CmdMesCod = models.ForeignKey(G1_MESA, on_delete=models.CASCADE)

class GZZ_ESTADO_PEDIDO(models.Model):
    EstPedCod = models.AutoField(verbose_name="Codigo de Estado Pedido:", primary_key=True)
    EstPedNom = models.CharField(verbose_name="Nombre de Estado Pedido:", max_length=20)
    EstPedDes = models.CharField(verbose_name="Descripcion de Estado Pedido:", max_length=50)

class G4Z_COMANDA_PRODUCTO(models.Model):
    CmdProCod = models.AutoField(verbose_name="Codigo Comanda Producto:", primary_key=True)
    CmdProCmdCod = models.ForeignKey(G1_PRODUCTO, on_delete=models.CASCADE)
    CmdProProCod = models.ForeignKey(G4_COMANDA, on_delete=models.CASCADE)
    CmdProCan = models.IntegerField(verbose_name="Cantidad de Producto")
    CmdProPreUni = models.FloatField(verbose_name="Precio de Unidad")
    CmdProEstPedCod = models.ForeignKey(GZZ_ESTADO_PEDIDO, on_delete=models.CASCADE)
