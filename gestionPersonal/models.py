from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class G1_ROL(models.Model):
    RolCod = models.AutoField(verbose_name="Codigo de Categoria:", primary_key=True)
    RolNom = models.CharField(verbose_name="Nombre de Categoria:", max_length=20)

class G1_USUARIO(AbstractUser):
    UsuDni = models.CharField(verbose_name="Dni Usuario:",max_length=8, unique=True)
    UsuCelular = models.CharField(verbose_name="Celular Usuario:",max_length=9)
    UsuDir = models.CharField(verbose_name="Direccion Usuario:",max_length=70)
    UsuSue = models.FloatField(verbose_name="Sueldo Usuario:")
    UsuImaNom = models.CharField(verbose_name="Nombre de Imagen Usuario:", max_length=10)
    UsuRolCod = models.ForeignKey(G1_ROL, on_delete=models.CASCADE)
    USERNAME_FIELD = 'UsuDni'
    class Meta:
        verbose_name = "g1_usuario"
