from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Tela de Login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # Rota de Logout
    path('logout/', views.fazer_logout, name='logout'),
    
    # Rotas existentes do app usuarios
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
]