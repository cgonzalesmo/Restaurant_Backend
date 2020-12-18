from django.db import models

# Create your models here.
class G1_MESA(models.Model):
    MesCod = models.AutoField(verbose_name="Codigo de Mesa:", primary_key=True)
    MesCap = models.IntegerField(verbose_name="Capacidad de Mesa:")
    MesDis = models.BooleanField(verbose_name="Descripcion de Mesa:", default=False)   
