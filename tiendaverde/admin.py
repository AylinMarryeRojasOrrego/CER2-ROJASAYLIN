from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Vendedor
from .models import Cliente
from .models import Producto



# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_vendedor', 'is_cliente')}),
    )

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Producto)