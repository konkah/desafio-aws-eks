from rest_framework import serializers
from .models import Tbl_Clientes, Tbl_Enderecos
from validate_docbr import CPF
import re

'''
Essa classe transforma os JSONs recebidos em objetos
na memória e vice-versa.
'''
class Tbl_ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Clientes
        fields = [
            'id',
            'nome_completo_cliente', 
            'cpf', 
            'email',
            'data_nascimento',
            'numero_telefone',
            'deletado',
        ]
    
    def validate_cpf(self, value):
        cpf = CPF()
        if not cpf.validate(value):
            raise serializers.ValidationError(
                'Não é um CPF válido!'
            )
        return value
    
    def validate_email(self, value):
        if not re.match('.+@.+\..+', value):
            raise serializers.ValidationError(
                'Não é um e-mail válido!'
            )
        return value

    def validate_numero_telefone(self, value):
        if not re.match('\(\d{2,3}\) ?\d{4,5}\-\d{4}', value):
            raise serializers.ValidationError(
                'Não é um telefone válido!'
            )
        return value

'''
Essa classe transforma os JSONs recebidos em objetos
na memória e vice-versa.
'''
class Tbl_EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Enderecos
        fields = [
            'id',
            'rua', 
            'numero', 
            'complemento',
            'cep',
            'cidade',
            'estado',
            'pais',
            'cliente',
            'cliente_id',
            'deletado',
        ]
    
    def validate_cep(self, value):
        if not re.match('\d{5}\-\d{3}', value):
            raise serializers.ValidationError(
                'Não é um CEP válido!'
            )
        return value
    
    '''
    Função que verifica se o ID do cliente existe
    e não pertence a um cliente deletado para inserir
    ou atualizar um endereço.
    '''
    def validate_cliente_id(self, cli_id):
        cliente = Tbl_Clientes.objects.get(pk = cli_id)
        if cliente.deletado:
            raise serializers.ValidationError(
                'Cliente inexistente.'
            )
        return cli_id