from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=100, blank=True, null=True, default='Rua do Sobe e desce')
    telefone = models.CharField(max_length=20, blank=True, null=True, default='(99) 9 9999-9999')
    idade = models.PositiveIntegerField(default=20)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return '%s' % self.nome
