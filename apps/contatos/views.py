from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.contatos.models import Contato


def lista_contatos(request):
    contatos = Contato.objects.all().order_by('nome')
    context = {
        'contatos': contatos
    }
    return render(request, 'contatos/contato_list.html', context)


class ContatoListView(ListView):
    model = Contato
    context_object_name = 'contatos'


class ContatoCreateView(CreateView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('lista_contatos_generica')


class ContatoUpdateView(UpdateView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('lista_contatos_generica')


class ContatoDeleteView(DeleteView):
    model = Contato
    success_url = reverse_lazy('lista_contatos')
