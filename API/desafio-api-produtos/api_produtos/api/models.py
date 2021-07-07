from django.db import models
import requests
from api_produtos.address import CLIENTES_API

class Tbl_Produtos(models.Model):
    nome_produto = models.CharField(max_length=200)
    preco_produto = models.FloatField()
    disponivel_produto = models.BooleanField()
    deletado = models.BooleanField()

    def __str__(self):
        return self.nome_produto

class Tbl_Inventarios(models.Model):
    cliente_id = models.IntegerField()
    produto_id = models.IntegerField()
    deletado = models.BooleanField()
    
    @property
    def cliente(self):
        url_cliente = "http://"+CLIENTES_API+"/clientes_api/" + str(self.cliente_id) + "/"
        return requests.get(url_cliente, auth=('admin','admin')).json()

    @property
    def produto(self):
        url_produto = "http://localhost/produtos_api/" + str(self.produto_id) + "/"
        return requests.get(url_produto, auth=('admin','admin')).json()
 
    def __str__(self):
        return self.produto() + ' de '+ self.cliente()