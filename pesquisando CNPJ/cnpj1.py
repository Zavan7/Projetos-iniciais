import requests
import json

def obter_dados(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    headers = {"User-Agent": "Mozilla/5.0"}
    
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro na solicitação:", resposta.status_code)
        return None

cnpj_ex = '00935820000175'
dados_empresa = obter_dados(cnpj_ex)

if dados_empresa:
    print(json.dumps(dados_empresa, indent=4))
