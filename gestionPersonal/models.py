from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class G1_USUARIO_MANAGER(BaseUserManager):
    def create_user(self, UsuDni, password=None):
        if not UsuDni:
            raise ValueError('El usuario debe tener DNI')
        user = self.model(
            UsuDni=UsuDni,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, UsuDni, password=None):
        user = self.create_user(
            UsuDni,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class G1_ROL(models.Model):
    RolCod = models.AutoField(verbose_name="Codigo de Categoria:", primary_key=True)
    RolNom = models.CharField(verbose_name="Nombre de Categoria:", max_length=20)

class G1_USUARIO(AbstractBaseUser):
    UsuCod = models.AutoField(verbose_name="Codigo de Usuario:", primary_key=True)
    UsuDni = models.CharField(verbose_name="Dni Usuario:",max_length=8, unique=True)
    UsuNom = models.CharField(verbose_name="Nombre Usuario:", max_length=50)
    UsuApePat = models.CharField(verbose_name="Apellido Paterno Usuario:", max_length=30)
    UsuApeMat = models.CharField(verbose_name="Apellido Materno Usuario:", max_length=30)
    UsuCelular = models.CharField(verbose_name="Celular Usuario:",max_length=9, blank=True, null=True)
    UsuDir = models.CharField(verbose_name="Direccion Usuario:",max_length=70, blank=True, null=True)
    UsuSue = models.FloatField(verbose_name="Sueldo Usuario:", blank=True, null=True)
    UsuImaNom = models.CharField(verbose_name="Nombre de Imagen Usuario:", max_length=10, blank=True, null=True)
    UsuRolCod = models.ForeignKey(G1_ROL, on_delete=models.CASCADE,blank=True, null=True)

    objects = G1_USUARIO_MANAGER()

    USERNAME_FIELD = 'UsuDni'
    class Meta:
        verbose_name = "g1_usuario"

    def __str__(self):
        return f'G1_USUARIO{self.UsuDni}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_staff