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
    
    # Rotas do App de Usuários
    path('usuarios/', include('usuarios.urls')),
    
    # Futuros apps do sistema LEEPER (descomentar à medida que forem criados):
    # path('materiais/', include('materiais.urls')),
    # path('movimentacoes/', include('movimentacoes.urls')),
    # path('alertas/', include('alertas.urls')),
]