from django.shortcuts import render

def listar_movimentacoes(request):
    return render(request, 'movimentacoes/listar.html')

# Create your views here.
