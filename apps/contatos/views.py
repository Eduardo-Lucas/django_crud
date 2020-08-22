from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from apps.contatos.models import Contato


def lista_contatos(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos
    }
    return render(request, 'contatos/contato_list.html', context)


class ContatoListView(ListView):
    model = Contato


class ContatoCreateView(CreateView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('lista_contatos')
