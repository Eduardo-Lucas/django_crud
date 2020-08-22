from django.urls import path

from apps.contatos.views import lista_contatos, ContatoListView, ContatoCreateView

urlpatterns = [
    path('lista', lista_contatos, name='lista_contatos'),
    path('lista_generica', ContatoListView.as_view(), name='lista_contatos_generica'),
    path('create', ContatoCreateView.as_view(), name='contato_create'),
]
