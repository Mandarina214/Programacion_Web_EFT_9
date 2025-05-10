from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50, choices=[
        ('sega', 'Sega'),
        ('nintendo', 'Nintendo'),
        ('atari', 'Atari'),
        ('playstation', 'PlayStation'),
        ('dreamcast', 'Dreamcast')
    ])  # o usar ForeignKey a un modelo Categoria si prefieres

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=20, choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta')])

    def __str__(self):
        return f"Venta de {self.producto.nombre} el {self.fecha}"

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    
    calle = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    tipo_direccion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - Perfil"