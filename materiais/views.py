from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Material

@login_required
def listar_materiais(request):
    materiais = Material.objects.all()
    return render(request, 'materiais/listar.html', {'materiais': materiais})