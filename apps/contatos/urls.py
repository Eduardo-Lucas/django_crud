from django.urls import path

from apps.contatos.views import lista_contatos, ContatoListView, ContatoCreateView, ContatoUpdateView, ContatoDeleteView

urlpatterns = [
    path('read', lista_contatos, name='lista_contatos'),
    path('lista_generica', ContatoListView.as_view(), name='lista_contatos_generica'),
    path('create', ContatoCreateView.as_view(), name='contato_create'),
    path('update/<int:pk>/', ContatoUpdateView.as_view(), name='contato_update'),
    path('delete/<int:pk>/', ContatoDeleteView.as_view(), name='contato_delete'),
]
