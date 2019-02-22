from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from pedido.views import CadastroUpdate
from pedido.views import CadastroDelete
from django.conf.urls import include

urlpatterns = [
    path('', views.CadastroListView.as_view(), name='cadastro-list'),
    url(r'(?P<pk>[0-9]+)/$', CadastroUpdate.as_view(), name='cadastro-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', CadastroDelete.as_view(), name='cadastro-delete'),
    path('cadastrar', views.index, name='index'),
    path('ajax/load-preco/', views.load_preco, name='load_preco'),
    path('ajax/load-rentabilidade/', views.load_rentabilidade, name='load_rentabilidade'),
    path('ajax/load-total/', views.load_total, name='load_total'),

]
