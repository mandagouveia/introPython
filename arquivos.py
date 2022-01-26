# 1 - importação de pacotes
import json
import pytest

# 2 - Classe


# 3 - Definições (Funções e Métodos)

dados = {'cliente': []}

dados['cliente'].append({
    'nome': 'Juca',
    'telefone': '11999999999',
    'email': 'juca@iterasys.com.br'
})
dados['cliente'].append({
    'nome': 'Ana',
    'telefone': '22999999999',
    'email': 'ana@iterasys.com.br'
})

def criar_json():
    with open('clientes.json', 'w') as outfile:
        json.dump(dados, outfile, indent=4)

def ler_json():
    with open('clientes.json') as outfile:
        dados = json.load(outfile)
        for registro in dados['cliente']:
            print('nome' + registro['nome'])
            print('telefone' + registro['telefone'])
            print('email' + registro['email'])

def ler_json_e_adicionar_json():
    with open('clientes.json') as outfile:
        dados = json.load(outfile)
        temp = []
        for registro in dados['cliente']:
            print('nome' + registro['nome'])
            print('telefone' + registro['telefone'])
            print('email' + registro['email'])
            temp = '\'nome\''+':'+registro['nome'] + + '\','\
                ',telefone: ' +registro['telefone']
def testar_criar_json():
    criar_json()
    print(dados['cliente'])

def testar_ler_json():
    print('Leitura do json por linha')
    ler_json()
    print(dados['cliente'])

