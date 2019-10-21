from django.shortcuts import render, redirect
from .models import Categoria, Transacao
from .forms import Categoriaform, TransacaoForm
import datetime

# Create your views here.
def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['carros'] = ['Siena','Corsa','Gol']
    return render(request, 'T004/home004.html', data)


def listCategorias(request):
    data = {}
    data['categorias'] = Categoria.objects.all()
    return render(request, 'T004/listCategorias.html', data)


def novaCategoria(request):
    data = {}
    form = Categoriaform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listCategorias')

    data['form'] = form
    return render(request, 'T004/cadCategorias.html', data)


def upCategoria(request, pk):
    data = {}
    categoria = Categoria.objects.get(pk=pk)
    form = Categoriaform(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('listCategorias')

    data['form'] = form
    data['categoria'] = categoria
    return render(request, 'T004/cadCategorias.html', data)


def deleteCat(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria.delete()
    return redirect('listCategorias')


def listTransacoes(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'T004/listTransacoes.html', data)


def novaTransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listTransacoes')

    data['form'] = form
    return render(request, 'T004/cadTransacoes.html', data)


def upTransacao(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('listTransacoes')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'T004/cadTransacoes.html', data)


def deleteTrans(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('listTransacoes')
