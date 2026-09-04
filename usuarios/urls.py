from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
]