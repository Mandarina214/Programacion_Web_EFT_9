from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import logout
from django.shortcuts import redirect


router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'ventas', views.VentaViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.register, name='register'),  
    path('logout/', lambda request: logout(request) or redirect('login'), name='logout'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/atari', views.categoria_atari, name='categoria_atari'),
    path('categorias/dreamcast', views.categoria_dreamcast, name='categoria_dreamcast'),
    path('categorias/nintendo', views.categoria_nintendo, name='categoria_nintendo'),
    path('categorias/playstation', views.categoria_playstation, name='categoria_playstation'),
    path('categorias/sega', views.categoria_sega, name='categoria_sega'),
    path('perfil/', views.perfil, name='perfil'),
    path('productos/', views.productos, name='productos'),
    path('productos/atari/atari_01', views.atari_01, name='atari_01'),
    path('productos/atari/atari_02', views.atari_02, name='atari_02'),
    path('productos/dreamcast/dreamcast_01', views.dreamcast_01, name='dreamcast_01'),
    path('productos/dreamcast/dreamcast_02', views.dreamcast_02, name='dreamcast_02'),
    path('productos/nintendo/nintendo_01', views.nintendo_01, name='nintendo_01'),
    path('productos/nintendo/nintendo_02', views.nintendo_02, name='nintendo_02'),
    path('productos/plastation/plastation_01', views.plastation_01, name='plastation_01'),
    path('productos/plastation/plastation_02', views.plastation_02, name='plastation_02'),
    path('productos/sega/sega_01', views.sega_01, name='sega_01'),
    path('productos/sega/sega_02', views.sega_02, name='sega_02'),
    path('api/juegos/', views.api_buscar_juego),
    path('api/usd-clp/', views.api_usd_a_clp),
    path('juegos/', views.vista_juegos),
    path('api/', include(router.urls)),  # <--- APIs propias aquí
]