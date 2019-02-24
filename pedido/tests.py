from django.test import TestCase
from pedido.models import Cadastro
from pedido.models import Produto
from pedido.models import Cliente
from pedido.forms import CadastroForm
import json
import unittest

class CadastroTestCase(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(nome="Nathália")
        self.item = Produto.objects.create(nome="Nathália's product", preco_unit=10)
        #self.quantidade=1

    def test_creates_record_correctly(self):
        cadastro = Cadastro.objects.create(
            cliente=self.cliente,
            item=self.item,
        )
        self.assertEqual(cadastro.cliente, self.cliente)
        self.assertEqual(cadastro.item, self.item)

    def test_str(self):
        cadastro = Cadastro.objects.create(
            cliente=self.cliente,
            item=self.item,
        )
        self.assertEqual(str(cadastro), '{} - {}'.format(self.cliente.nome, self.item.nome))

    def test_form(self):
        cadastro = CadastroForms(
            cliente=self.cliente,
            item=self.item,
        )
        self.assertEqual
