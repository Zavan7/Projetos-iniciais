'''Recebo o CEP do usuario, e forneço o endereço desse CEP fornecido'''

import http.client
import pandas as pd
import json
from datetime import datetime

def obter_end_cep(cep):
    conexao = http.client.HTTPSConnection('viacep.com.br')
    conexao.request('GET', f'/ws/{cep}/json/')
    resposta = conexao.getresponse()
    dados = resposta.read()
    endereco = json.loads(dados.decode('utf-8'))
    conexao.close()
    return endereco

def salvar_excel(end, cep):
    if 'erro' not in end:
        # Gera um nome de arquivo único com data e hora
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_arquivo = f'endereco_{cep}_{timestamp}.xlsx'
        
        df = pd.DataFrame([end])
        df.to_excel(nome_arquivo, index=False)
        print(f'Dados salvos com sucesso no arquivo: {nome_arquivo}')
    else:
        print(f'Não foi possível salvar os dados para o CEP {cep}: CEP não encontrado')

# Exemplo de uso: usuário fornece um CEP e o código gera um arquivo com nome único
cep_input = input("Digite um CEP: ")
end_resultado = obter_end_cep(cep_input)
salvar_excel(end_resultado, cep_input)