from django.shortcuts import render, redirect
from .models import Nerd
from .forms import NerdForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def todos(request):
    nerds = Nerd.objects.all().order_by('nome')
    return render(request, 'todos.html', {'nerds': nerds})

def detalhar(request, id):
    nerd = Nerd.objects.get(id=id)
    return render(request, 'detalhar.html', {'nerd': nerd})

def sugerir(request):
    if request.method == 'POST':
        form = NerdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Nerd cadastrado com Sucesso!")
            return redirect('todos')
        
    else:
        form = NerdForm()
        return render(request, 'sugerir.html', {'form': form})
    
def atualizar(request, id):
    nerd = Nerd.objects.get(id=id)
    form = NerdForm(instance=nerd)
    if request.method == "POST":
        form = NerdForm(request.POST, request.FILES, instance=nerd)
        if form.is_valid():
            form.save()
            return redirect("atualizar", id=id)
        else:
            return render(request, 'atualizar.html', {'form': form})
        
    else:
        return render(request, 'atualizar.html', {'form': form})
    
def apagar(request, id):
    nerd = Nerd.objects.get(id=id)
    nerd.delete()
    messages.add_message(request, messages.SUCCESS, "Nerd apagado com Sucesso!")
    return redirect('todos')

def sobre(request):
    return render(request, 'sobre.html')