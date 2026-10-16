"""
URL configuration for setup project.
"""
from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuarios_views

urlpatterns = [
    # Página Inicial (acesso direto em http://127.0.0.1:8000/)
    path('', usuarios_views.index, name='index'),
    
    # Painel de administração do Django
    path('admin/', admin.site.urls),
    
    # Rotas dos Apps do sistema LEEPER
    path('usuarios/', include('usuarios.urls')),
    path('materiais/', include('materiais.urls')),
    path('movimentacoes/', include('movimentacoes.urls')),
]