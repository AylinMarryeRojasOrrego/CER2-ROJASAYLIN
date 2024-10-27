from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vendedor
from .models import Cliente
from .models import Producto



# Register your models here.


admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Producto)