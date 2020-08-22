from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    idade = models.PositiveIntegerField(default=20)

    def __str__(self):
        return '%s' % self.nome
