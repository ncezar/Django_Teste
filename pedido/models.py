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
    nome= models.CharField(max_length=200,blank=False, null=False)
    preco_unit = models.FloatField(max_length=200)
    multiplo = models.IntegerField(default=0, null=False)
    def __str__(self):
        return '{} '.format(self.nome)

class Cadastro(models.Model):
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE, null=False, blank=False)
    item = models.ForeignKey('Produto',on_delete=models.CASCADE,null=False, blank=False)
    preco_unitario =models.FloatField(default=0)
    quantidade = models.IntegerField(default=0)
    total = models.FloatField(null=False, default=0)
    def __str__(self):
      return '{} - {}'.format(self.cliente.nome, self.item.nome)
    def get_absolute_url(self):
      return reverse('cadastro-update', kwargs={'pk': self.pk})
