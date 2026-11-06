from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Movimentacao

@login_required
def listar_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data_movimentacao')
    return render(request, 'movimentacoes/listar.html', {'movimentacoes': movimentacoes})