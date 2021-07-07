from django.db import models
import requests


# Classe Tbl_Clientes vira uma tabela no MySQL
class Tbl_Clientes(models.Model):
    nome_completo_cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    numero_telefone = models.CharField(max_length=15)
    deletado = models.BooleanField()
    
    '''
    Se for feito pedido um texto representativo
    do cliente, será retornado o nome (string).
    '''
    def __str__(self):
        return self.nome_completo_cliente

# Classe Tbl_Enderecos vira uma tabela no MySQL
class Tbl_Enderecos(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    cliente_id = models.IntegerField()
    deletado = models.BooleanField()

    '''
    Uma função que busca os dados dos clientes na API Clientes
    através do ID.
    '''
    @property
    def cliente(self):
        url_cliente = "http://localhost/clientes_api/" + str(self.cliente_id) + "/"
        return requests.get(url_cliente, auth=('admin','admin')).json()

    '''
    Se for feito pedido um texto representativo
    do endereço, será retornado a rua e o número (strings).
    '''
    def __str__(self):
        return self.rua + ', ' + self.numero