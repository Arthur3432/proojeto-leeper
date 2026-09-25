from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Usuario

def index(request):
    return render(request, 'usuarios/index.html')

def listar_usuarios(request):
    return render(request, 'usuarios/listar.html')

def cadastrar_usuario(request):
    return render(request, 'usuarios/cadastrar.html')