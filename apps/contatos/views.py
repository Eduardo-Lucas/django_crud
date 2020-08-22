from django.shortcuts import render
from django.views.generic import ListView, CreateView

from apps.contatos.models import Contato


def lista_contatos(request):
    return render(request, 'contatos/contato_list.html')


class ContatoListView(ListView):
    model = Contato


class ContatoCreateView(CreateView):
    model = Contato
    fields = '__all__'
