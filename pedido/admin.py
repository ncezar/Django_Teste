from django.contrib import admin
from .models import Cliente
from .models import Produto
from .models import Cadastro
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco_unit', 'multiplo']

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'item', 'preco_unitario', 'quantidade', 'total']
