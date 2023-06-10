from django.shortcuts import redirect, render
from . models import Pessoas 

# Create your views here.

def home(request):
    pessoas = Pessoas.objects.all()
    return render(request, 'pessoas/index.html', {"pessoas":pessoas})


def create(request):
    vnome = request.POST.get("nome")
    Pessoas.objects.create(nome=vnome)
    return redirect(home)


def edit(request, id):
    pessoa = Pessoas.objects.get(id=id)
    return render(request, 'pessoas/update.html', {"pessoa":pessoa})


def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoas.objects.get(id=id)
    pessoa.nome=vnome
    pessoa.save()
    return redirect(home)


def delete(request, id):
    pessoa = Pessoas.objects.get(id=id)
    pessoa.delete()
    return redirect(home)