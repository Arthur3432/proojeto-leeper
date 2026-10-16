from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_movimentacoes, name='listar_movimentacoes'),
]