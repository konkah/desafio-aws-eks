from django.shortcuts import render
from .models import Tbl_Clientes, Tbl_Enderecos
from .serializers import Tbl_ClientesSerializer, Tbl_EnderecosSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


'''
Essa classe pega os objetos do Models e usa a serialização
do Serializers para criar as urls da API que retornam os dados
do banco de dados.
'''
class Tbl_ClientesViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Clientes.objects.all()
    serializer_class = Tbl_ClientesSerializer

    '''
    Essa função substitui a função nativa de delete
    do ModelViewSet e marca o cliente como "deletado"
    no banco de dados.
    '''
    def destroy(self,request,pk=None):
        cliente = Tbl_Clientes.objects.get(pk = pk)
        cliente.deletado = True
        cliente.save()
        return Response({"detail":"Cliente deletado com sucesso!"})

class Tbl_EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Enderecos.objects.all()
    serializer_class = Tbl_EnderecosSerializer

    '''
    Essa função substitui a função nativa de delete
    do ModelViewSet e marca o endereço como "deletado"
    no banco de dados.
    '''
    def destroy(self,request,pk=None):
        endereco = Tbl_Enderecos.objects.get(pk = pk)
        endereco.deletado = True
        endereco.save()
        return Response({"detail":"Endereço deletado com sucesso!"})