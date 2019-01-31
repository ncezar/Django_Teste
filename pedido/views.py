from django.shortcuts import render
from .forms import CadastroForm
from .forms import Cadastro
from .forms import Produto
from django.contrib import messages
from django.utils import timezone
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
<<<<<<< 9f9ffdd18c4322d695dfc86a253abb00b4c8b198
<<<<<<< HEAD
from django.contrib import messages
=======
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281
=======
from django.contrib import messages
>>>>>>> erros finais corrigidos

def base(request):
    return render(request, "pedido/base.html")
#-----#
def index(request): #CadastroCreate
    if request.method=='POST':
        form = CadastroForm(request.POST or None)
        if form.is_valid():
<<<<<<< 9f9ffdd18c4322d695dfc86a253abb00b4c8b198
<<<<<<< HEAD
=======
            preco_unitario = request.POST.get("preco_unitario")
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281
=======
>>>>>>> erros finais corrigidos
            messages.success(request, 'Enviado com sucesso!')
            form.save()
    else:
        form = CadastroForm()
    context = {'form': form}
    return render(request, "pedido/index.html", context)
#-----#
class CadastroListView(ListView):
    model = Cadastro
    template_name = "pedido/base.html"


    def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        context = super(CadastroListView, self).get_context_data(**kwargs)
        return context
#-----#
class CadastroUpdate(UpdateView):
    model = Cadastro
    form_class = CadastroForm
    template_name="pedido/index.html"
    success_url = ('/')

#-----#
class CadastroDelete(DeleteView):
    model = Cadastro
    success_url = reverse_lazy('pedido/base.html')

#-----#
def load_preco(request):
    item = request.GET.get('item')
<<<<<<< 9f9ffdd18c4322d695dfc86a253abb00b4c8b198
    print(item)
    produto = Produto.objects.get(id=item)
    return JsonResponse({'preco_unitario' : produto.preco_unit})
    #return render(request, {'preco_unitario': produto.preco_unit})
<<<<<<< HEAD
=======
    #print(item)
    produto = Produto.objects.get(id=item)
    return JsonResponse({'preco_unitario' : produto.preco_unit})
    #return render(request, {'preco_unitario': produto.preco_unit})
>>>>>>> erros finais corrigidos
#---#
def load_rentabilidade(request):
    item = request.GET.get('item')
    preco_unitario = request.GET.get('preco_unitario')
    #print(preco_unitario)
    produto = Produto.objects.get(id=item)#estou pegando o preco da tabela de mesmo item selecionado pra comparar com o q usuario digitou
<<<<<<< 9f9ffdd18c4322d695dfc86a253abb00b4c8b198

    data={
        'rent_otima': (float(preco_unitario) > produto.preco_unit),
        'rent_boa': (float(preco_unitario) >= (produto.preco_unit*0.9) and float(preco_unitario <=(produto.preco_unit)) or float(preco_unitario))

    }

    return JsonResponse(data)
=======
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281
=======
    data={
        'rent_otima': (float(preco_unitario) > produto.preco_unit),
        'rent_boa': (float(preco_unitario) >= (produto.preco_unit*0.9) and float(preco_unitario)<= (produto.preco_unit) )
    }
    return JsonResponse(data)
>>>>>>> erros finais corrigidos
