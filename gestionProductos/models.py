from django.db import models

# Create your models here.
class GZZ_PRODUCTO_CATEGORIA(models.Model):
    ProCatCod = models.AutoField(verbose_name="Codigo de Categoria:", primary_key=True)
    ProCatNom = models.CharField(verbose_name="Nombre de Categoria:", max_length=20)
    ProCatDes = models.CharField(verbose_name="Descripcion de Categoria:", max_length=50)
    ProCatImaNom = models.CharField(verbose_name="Nombre de Imagen Categoria:", max_length=10)

class G1_PRODUCTO(models.Model):
    ProCod = models.AutoField(verbose_name="Codigo de Producto:", primary_key=True)
    ProNom = models.CharField(verbose_name="Nombre de Producto:", max_length=30)
    ProPreVen = models.FloatField(verbose_name="Precio de Producto:")
    ProImaNom = models.CharField(verbose_name="Nombre de Imagen Producto:", max_length=10)
    ProCatCod = models.ForeignKey(GZZ_PRODUCTO_CATEGORIA, on_delete=models.CASCADE)
    ProDis = models.BooleanField(verbose_name= "Producto Disponible")
