from rest_framework import serializers
from .models import Tbl_Produtos, Tbl_Inventarios
import requests
from api_produtos.address import CLIENTES_API

class Tbl_ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Produtos
        fields = [
            'id',
            'nome_produto', 
            'preco_produto', 
            'disponivel_produto',
            'deletado',
        ]

class Tbl_InventariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Inventarios
        fields = [
            'id',
            'produto',
            'produto_id', 
            'cliente',
            'cliente_id',
            'deletado',
        ]
        depth = 1

    def validate_cliente_id(self, cliente_id):
        url_cliente = "http://"+CLIENTES_API+"/clientes_api/" + str(cliente_id) + "/"
        cliente = requests.get(url_cliente, auth=('admin','admin')).status_code
        if cliente >= 500:
            raise serializers.ValidationError(
                'Problema ao tentar encontrar cliente.'
            )
        if cliente >= 400:
            raise serializers.ValidationError(
                'Cliente não encontrado.'
            )
        return cliente_id

    def validate_produto_id(self, produto_id):
        produto = Tbl_Produtos.objects.get(pk = produto_id)
        if not produto.disponivel_produto:
            raise serializers.ValidationError(
                'Produto não disponível para compra.'
            )
        if produto.deletado:
            raise serializers.ValidationError(
                'Produto inexistente.'
            )
        return produto_id