from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_vendedor = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)

class Vendedor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Cliente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return ' %s por %s' % (self.nombre, self.precio)
