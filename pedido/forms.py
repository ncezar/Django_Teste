from django import forms
from .models import Cadastro
from .models import Produto

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['cliente', 'item', 'preco_unitario', 'quantidade']
        #---#
<<<<<<< 9f9ffdd18c4322d695dfc86a253abb00b4c8b198
    def clean_preco_unitario(self):
        preco_unitario = self.cleaned_data['preco_unitario']
        if preco_unitario <= 0:
            raise forms.ValidationError("O preço precisa ser maior que 0!")
<<<<<<< HEAD
        return self.cleaned_data
=======
        return preco_unitario
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281
    #---#

=======
>>>>>>> erros finais corrigidos

    def clean(self):
        item = self.cleaned_data['item']
        quantidade = self.cleaned_data['quantidade']
        preco_unitario = self.cleaned_data['preco_unitario']
<<<<<<< 9f9ffdd18c4322d695dfc86a253abb00b4c8b198
<<<<<<< HEAD
        #preco_unitario = item.preco_unit
        print('Item.Preco_unit',item.preco_unit)
        print('Preco_Unit',preco_unitario)#item ja é objeto de Produto, logo ele alcança os valores dos campos desta tabela, logo é só comprar com a quantidade
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade precisa ser maior que 0!")
        if (({'preco_unitario': preco_unitario}) < ((item.preco_unit)*0.9)):
            raise forms.ValidationError("Rentabilidade ruim!")
        if (quantidade % (item.multiplo)) !=0:
=======
        #print(item.multiplo) item ja é objeto de Produto, logo ele alcança os valores dos campos desta tabela, logo é só comprar com a quantidade
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade precisa ser maior que 0!")
        if (preco_unitario <= ((item.preco_unit)-(item.preco_unit*0.1))):
            raise forms.ValidationError("Rentabilidade ruim!")
        if (quantidade %( item.multiplo)) !=0:
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281
            raise forms.ValidationError("A quantidade precisa multipla de: %s" %(item.multiplo))
=======
        #preco_unitario = item.preco_unit
        print('Item.Preco_unit',item.preco_unit)
        print('Preco_Unit',self.cleaned_data['preco_unitario'])#item ja é objeto de Produto, logo ele alcança os valores dos campos desta tabela, logo é só comprar com a quantidade
        if preco_unitario <= 0:
            raise forms.ValidationError("O preço precisa ser maior que 0!")
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade precisa ser maior que 0!")
        if ((preco_unitario) < ((item.preco_unit)*0.9)):
            raise forms.ValidationError("Rentabilidade ruim!")
        if (item.multiplo) > 0:
            if (quantidade % (item.multiplo)) !=0:
               raise forms.ValidationError("A quantidade precisa multipla de: %s" %(item.multiplo))
>>>>>>> erros finais corrigidos
        return self.cleaned_data
