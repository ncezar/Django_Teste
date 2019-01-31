from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from pedido.views import CadastroUpdate, CadastroDelete
from django.conf.urls import include

urlpatterns = [
    #path('', views.base, name='base'),
    path('', views.CadastroListView.as_view(), name='cadastro-list'),
    url(r'(?P<pk>[0-9]+)/$', CadastroUpdate.as_view(), name='cadastro-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', CadastroDelete.as_view(), name='cadastro-delete'),
    path('cadastrar', views.index, name='index'),
    path('ajax/load-preco/', views.load_preco, name='load_preco'),
<<<<<<< HEAD
    path('ajax/load-rentabilidade/', views.load_rentabilidade, name='load_rentabilidade'),
    #path('load-rentabilidade/', views.load_preco, name='load_rentabilidade'),

=======
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281


]
