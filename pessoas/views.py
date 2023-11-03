from django.shortcuts import redirect, render
from . models import Pessoas 

# Create your views here.

def home(request):
    """
    Render the 'index.html' template with all instances of the 'Pessoas' model.

    Args:
        request (HttpRequest): The HTTP request object containing information about the current request.

    Returns:
        HttpResponse: The response object that renders the 'index.html' template with the retrieved instances of the 'Pessoas' model as a context variable.
    """
    pessoas = Pessoas.objects.all()
    return render(request, 'pessoas/index.html', {"pessoas": pessoas})


def create(request):
    """
    Create a new instance of the 'Pessoas' model based on the data received from a POST request and redirect the user back to the 'home' function.

    Args:
        request (HttpRequest): The HTTP request object containing information about the current request.

    Returns:
        HttpResponseRedirect: The response object that redirects the user back to the 'home' function.
    """
    vnome = request.POST.get("nome")
    Pessoas.objects.create(nome=vnome)
    return redirect(home)


def edit(request, id):
    """
    Retrieve a specific 'Pessoas' object from the database based on the provided 'id' parameter and render the 'update.html' template with the retrieved object.

    Args:
        request (object): The HTTP request object containing information about the request made by the user.
        id (int): The unique identifier of the 'Pessoas' object to be retrieved.

    Returns:
        object: The rendered template 'update.html' with the retrieved 'Pessoas' object as context.
    """
    pessoa = Pessoas.objects.get(id=id)
    return render(request, 'pessoas/update.html', {"pessoa": pessoa})


def update(request, id):
    """
    Update the 'nome' attribute of a 'Pessoas' object with the value obtained from the POST request and save the changes to the database. Redirect the user to the 'home' view.

    Args:
        request (object): The HTTP request object containing information about the request made by the user.
        id (int): The unique identifier of the 'Pessoas' object to be updated.

    Returns:
        object: Redirect to the 'home' view.
    """
    vnome = request.POST.get("nome")
    pessoa = Pessoas.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)


def delete(request, id):
    """
    Delete a record from the Pessoas model.

    Args:
        request: The HTTP request object.
        id: The ID of the record to be deleted.

    Returns:
        None

    Raises:
        Pessoas.DoesNotExist: If the record with the given ID does not exist.
    """
    pessoa = Pessoas.objects.get(id=id)
    pessoa.delete()
    return redirect(home)