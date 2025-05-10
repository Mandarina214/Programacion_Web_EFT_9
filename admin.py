from django.contrib import admin
from .models import Producto, Venta, PerfilUsuario

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(PerfilUsuario)
