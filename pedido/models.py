from django.urls import reverse
from django.db import models
from django.db import models
from django import forms


# Create your models here.
class Cliente(models.Model):
    nome= models.CharField(max_length=200)
    def __str__(self):
        return str(self.nome)

class Produto(models.Model):
    nome= models.CharField(max_length=200)
    preco_unit = models.FloatField(max_length=200)
    multiplo = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return '{} '.format(self.nome)

class Cadastro(models.Model):
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE,)
    item = models.ForeignKey('Produto',on_delete=models.CASCADE,)
    preco_unitario =models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    def __str__(self):
      return '{} - {}'.format(self.cliente.nome, self.item.nome)
    def get_absolute_url(self):
      return reverse('cadastro-update', kwargs={'pk': self.pk})
