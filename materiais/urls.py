from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_materiais, name='listar_materiais'),
]