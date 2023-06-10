from django.shortcuts import redirect, render
from . models import Pessoas 

# Create your views here.

def pessoas(request):
    pessoas = Pessoas.objects.all()
    return render(request, 'index.html', {"pessoas":pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    Pessoas.objects.create(nome=vnome)
    # pessoas = Pessoas.objects.all()
    # return render(request, 'index.html', {"pessoas":pessoas})
    return redirect(pessoas)


def editar(request, id):
    pessoa = Pessoas.objects.get(id=id)
    return render(request, 'update.html', {"pessoa":pessoa})


def update(request, id):
    vnome = request.POST.get("nome")
    
    pessoa = Pessoas.objects.get(id=id)
    pessoa.nome=vnome
    pessoa.save()
    return redirect(pessoas)

def delete(request, id):
    pessoa = Pessoas.objects.get(id=id)
    pessoa.delete()
    return redirect(pessoas)