"""
URL configuration for setup project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Painel de administração do Django
    path('admin/', admin.site.urls),
    
    # Rotas do App de Usuários
    path('usuarios/', include('usuarios.urls')),
    
    # Futuros apps do sistema LEEPER (descomente à medida que for criando os apps):
    # path('', include('core.urls')),              # Página Inicial / Dashboard
    # path('materiais/', include('materiais.urls')),  # Gerenciamento de materiais
    # path('movimentacoes/', include('movimentacoes.urls')), # Entradas e saídas
    # path('alertas/', include('alertas.urls')),    # Notificações de estoque mínimo
]