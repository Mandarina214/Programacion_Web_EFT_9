from django.shortcuts import render
from django.http import JsonResponse
from .apis_externas import buscar_juego, usd_a_clp
from rest_framework import viewsets
from .models import Producto, Venta
from .serializers import ProductoSerializer, VentaSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import PerfilUsuario
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # redirige a página principal
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')

        calle = request.POST.get('calle')
        numero = request.POST.get('numero')
        tipo_direccion = request.POST.get('tipo_direccion')

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El usuario ya existe'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = nombres
        user.last_name = apellidos
        user.save()

        perfil = PerfilUsuario.objects.create(
            user=user,
            nombres=nombres,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            calle=calle,
            numero=numero,
            tipo_direccion=tipo_direccion
        )

        return redirect('login')

    return render(request, 'registro.html')


def categorias(request):
    return render(request, './categorias/todas.html')

def categoria_atari(request):
    return render(request, './categorias/atari.html')

def categoria_dreamcast(request):
    return render(request, './categorias/dreamcast.html')

def categoria_nintendo (request):
    return render(request, './categorias/nintendo.html')

def categoria_playstation (request):
    return render(request, './categorias/playstation.html')

def categoria_sega (request):
    return render(request, './categorias/sega.html')

def perfil(request):
    return render(request, './perfil/perfil.html')

def productos(request):
    return render(request, './productos/producto.html')

def atari_01(request):
    return render(request, './productos/atari/atari_01.html')

def atari_02(request):
    return render(request, './productos/atari/atari_02.html')

def dreamcast_01(request):
    return render(request, './productos/dreamcast/dreamcast_01.html')

def dreamcast_02(request):
    return render(request, './productos/dreamcast/dreamcast_02.html')

def nintendo_01(request):
    return render(request, './productos/nintendo/nintendo_01.html')

def nintendo_02(request):
    return render(request, './productos/nintendo/nintendo_02.html')

def plastation_01(request):
    return render(request, './productos/plastation/plastation_01.html')

def plastation_02(request):
    return render(request, './productos/plastation/plastation_02.html')

def sega_01(request):
    return render(request, './productos/sega/sega_01.html')

def sega_02(request):
    return render(request, './productos/sega/sega_02.html')

def juegos(request):
    return render(request, "juegos.html")

def api_buscar_juego(request):
    nombre = request.GET.get('q', 'Halo')
    data = buscar_juego(nombre)
    return JsonResponse(data)

def api_usd_a_clp(request):
    data = usd_a_clp()
    return JsonResponse({"clp_por_usd": data.get("conversion_rate")})


def vista_juegos(request):
    query = request.GET.get("q", "Mario")
    data = buscar_juego(query)
    juegos = data.get("results", [])

    # Obtener tasa de cambio CLP
    tasa_data = usd_a_clp()
    tasa_clp = tasa_data.get("conversion_rate", 900)

    # Simular precio en USD para cada juego (ej: $30) y calcular CLP
    for juego in juegos:
        precio_usd = 30  # puedes cambiarlo o hacerlo aleatorio
        juego["precio_usd"] = precio_usd
        juego["precio_clp"] = round(precio_usd * tasa_clp)

    return render(request, "juegos.html", {
        "juegos": juegos,
        "query": query,
        "tasa": tasa_clp
    })

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer