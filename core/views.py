from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (Pessoa, 
    Veiculo,
    MovRotativos,
    Mensalista
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm
)


def home(request):
    return render(request, 'core/index.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form} 
    return render(request,'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def pessoa_update(request,id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoas.html',data)

def pessoa_delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    if(request.method == 'POST'):
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request,'core/delete_pessoa.html', {'pessoa':pessoa})


def lista_movRotativo(request):
    veiculos = MovRotativos.objects.all()
    form = MovRotativoForm()
    data = {'veiculos':veiculos, 'form':form} 
    return render(request, 'core/lista_rotativos.html', data)

def movRotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_rotativos')

def movRotativo_update(request,id):
    data = {}
    movRotativo = MovRotativos.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movRotativo)
    data['movRotativo'] = movRotativo
    data['form'] = form

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('core_lista_rotativos')
    else:
        return render(request,'core/update_movRotativos.html',data)

def movRotativo_delete(request,id):
    movRotativo = MovRotativos.objects.get(id=id)
    if(request.method == 'POST'):
        movRotativo.delete()
        return redirect('core_lista_rotativos')
    else:
        return render(request,'core/delete_movRotativo.html', {'movRotativo':movRotativo})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos':veiculos, 'form':form} 
    return render(request,'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def veiculo_update(request,id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request,'core/update_veiculos.html',data)

def veiculo_delete(request,id):
    veiculo = Veiculo.objects.get(id=id)
    if(request.method == 'POST'):
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request,'core/delete_veiculo.html', {'veiculo':veiculo})


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas':mensalistas, 'form':form} 
    return render(request,'core/lista_mensalista.html', data)

def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')

def mensalista_update(request,id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request,'core/update_mensalista.html',data)

def mensalista_delete(request,id):
    mensalista = Mensalista.objects.get(id=id)
    if(request.method == 'POST'):
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request,'core/delete_mensalista.html', {'mensalista':mensalista})
