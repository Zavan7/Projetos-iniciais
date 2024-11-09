import http.client
import json
import pandas as pd

def obter_endereco_cep(cep):
    conexao = http.client.HTTPConnection('viacep.com.br')
    conexao.request('GET', f'/ws/{cep}/json/')
    resposta = conexao.getresponse()
    if resposta.status != 200:
        conexao.close()
        return None
    dados = resposta.read()
    endereco = json.loads(dados.decode('utf-8'))
    conexao.close()
    return endereco if 'erro' not in endereco else None


caminho_planilha = 'CEP.xlsx'
planilha_ceps = pd.read_excel(caminho_planilha, sheet_name='CEP')
ceps = planilha_ceps['CEP'].dropna()
resultados = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF'])

for cep in ceps:
    endereco = obter_endereco_cep(str(cep).replace(',', ''))
    if endereco:
        nova_linha = pd.DataFrame([{
            'CEP': cep,
            'Logradouro': endereco.get('logradouro', ''),
            'Bairro': endereco.get('bairro', ''),
            'Localidade': endereco.get('localidade', ''),
            'UF': endereco.get('uf', ''),
        }])
        # Adiciona a nova linha ao DataFrame resultados
        resultados = pd.concat([resultados, nova_linha], ignore_index=True)

# Salvando os resultados na planilha
with pd.ExcelWriter(caminho_planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    resultados.to_excel(writer, sheet_name='Dados', index=False)

print("Endereços salvos na aba 'Dados' na planilha 'CEP.xlsx'.")
