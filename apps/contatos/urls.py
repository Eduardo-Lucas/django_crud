from django.urls import path

from apps.contatos.views import lista_contatos, ContatoListView, ContatoCreateView, ContatoUpdateView, ContatoDeleteView

urlpatterns = [
    # CRUD da class Contato
    path('create', ContatoCreateView.as_view(), name='contato_create'),
    path('read', ContatoListView.as_view(), name='lista_contatos_generica'),
    path('update/<int:pk>/', ContatoUpdateView.as_view(), name='contato_update'),
    path('delete/<int:pk>/', ContatoDeleteView.as_view(), name='contato_delete'),
]
