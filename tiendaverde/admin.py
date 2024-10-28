from django.contrib import admin
from .models import *

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register([Producto, Carrito, CarritoItem])
