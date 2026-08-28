from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Usuario

@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

@login_required
def cadastrar_usuario(request):
    # Apenas professores têm permissão para cadastrar novos usuários (RN01)
    if not request.user.is_professor():
        messages.error(request, "Acesso negado. Apenas professores podem realizar esta ação.")
        return redirect('listar_usuarios')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('listar_usuarios')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'usuarios/cadastrar.html', {'form': form})