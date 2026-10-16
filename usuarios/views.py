from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Usuario


def fazer_logout(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    return render(request, 'usuarios/index.html')


@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})


@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/cadastrar.html', {'form': form})