from django.urls import include, path
from .views import (
    home,
    lista_pessoas, 
    lista_veiculos, 
    lista_movRotativo,
    lista_mensalista,
    pessoa_novo,
    veiculo_novo,
    movRotativo_novo,
    mensalista_novo,
    veiculo_update,
    pessoa_update,
    mensalista_update,
    movRotativo_update,
    pessoa_delete,
    veiculo_delete,
    mensalista_delete,
    movRotativo_delete
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<id>',pessoa_update, name='core_pessoa_update'),
    path('pessoa_delete/<id>',pessoa_delete, name='core_pessoa_delete'),

    path('veiculo_novo', veiculo_novo, name='core_veiculo_novo'),
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_update/<id>',veiculo_update, name='core_veiculo_update'),
    path('veiculo_delete/<id>',veiculo_delete, name='core_veiculo_delete'),

    path('mensalista_novo', mensalista_novo, name='core_mensalista_novo'),
    path('mensalistas', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista_update/<id>',mensalista_update, name='core_mensalista_update'),
    path('mensalista_delete/<id>',mensalista_delete, name='core_mensalista_delete'),

    path('movrotativo_novo', movRotativo_novo, name='core_movrotativo_novo'),
    path('rotativos', lista_movRotativo, name='core_lista_rotativos'),
    path('movRotativo_update/<id>',movRotativo_update, name='core_movRotativo_update'),
    path('movRotativo_delete/<id>',movRotativo_delete, name='core_movRotativo_delete'),
]
