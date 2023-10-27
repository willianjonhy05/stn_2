from typing import Any
from django.shortcuts import render, redirect
from .models import Nerd
from .forms import NerdForm
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class Sobre(TemplateView):
    template_name = "sobre.html"


class Todos(TemplateView):
    template_name = "todos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nerds = Nerd.objects.all().order_by('nome')
        context['nerds'] = nerds
        return context


class Detalhar(TemplateView):
    template_name = "detalhar.html"

    def get(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nerd = Nerd.objects.get(id=kwargs['id'])
        context['nerd'] = nerd
        return context

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

