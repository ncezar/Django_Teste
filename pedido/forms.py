from django import forms
from .models import Cadastro
from .models import Produto

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['cliente', 'item', 'preco_unitario', 'quantidade']
        #---#
    def clean_preco_unitario(self):
        preco_unitario = self.cleaned_data['preco_unitario']
        if preco_unitario <= 0:
            raise forms.ValidationError("O preço precisa ser maior que 0!")
        return preco_unitario
    #---#
    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade precisa ser maior que 0!")
        return quantidade
    def clean(self):
        item = self.cleaned_data['item']
        quantidade = self.cleaned_data['quantidade']
        #preco_unitario = item.preco_unit
        #print(item.multiplo) item ja é objeto de Produto, logo ele alcança os valores dos campos desta tabela, logo é só comprar com a quantidade

        if (quantidade %( item.multiplo)) !=0:
            raise forms.ValidationError("A quantidade precisa multipla de: %s" %(item.multiplo))
        return self.cleaned_data
