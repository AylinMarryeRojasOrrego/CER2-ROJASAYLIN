from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

import uuid


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

#CARRITO COSAS

class Producto(models.Model):
    ide = models.UUIDField(default=uuid.uuid4, primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return ' %s por %s' % (self.nombre, self.precio)

class Carrito(models.Model):
    ide = models.UUIDField(default=uuid.uuid4, primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    pendiente_de_entrega = models.BooleanField(default=True)

    def __str__(self):
        return f"{str(self.ide)} de usuario {self.usuario}. Estado: {self.completado}. pendiente_de_entrega: {self.pendiente_de_entrega}"

    @property
    def precio_total(self):
        cosas_del_carrito = self.cosas_del_carrito.all()
        return sum([item.precio for item in cosas_del_carrito])

    @property
    def cantidad_de_cosas(self):
        cosas_del_carrito = self.cosas_del_carrito.all()
        return sum([item.cantidad for item in cosas_del_carrito])

class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="cosas_del_carrito")
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cantidad} x {self.producto}"

    @property
    def precio(self):
        return self.producto.precio * self.cantidad


