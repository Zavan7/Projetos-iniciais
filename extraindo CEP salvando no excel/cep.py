import http.client
import json
import pandas as pd
import openpyxl

def obter_end_cep(cep):
    conexao = http.client.HTTPSConnection('viacep.com.br')
    conexao.request('GET', f'/ws/{cep}/json/')
    resposta = conexao.getresponse()
    dados = resposta.read()
    endereco = json.loads(dados.decode('utf-8'))
    conexao.close()

    if 'erro' not in endereco:
        return endereco
    else:
        return 'CEP não encontrado'

cep_ex = '17055-180'
end_result = obter_end_cep(cep_ex)

print(end_result)
