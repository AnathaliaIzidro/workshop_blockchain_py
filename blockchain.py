# workshop blockchain
# Abrir o terminal do VS e digitar python -m venv venv   E depois digitar venv\Script\activate
# Caso o segundo passo não de certo  Abrir o power shell como administrador e digitar (pesquisar no youtube)
# instalar o requests no terminal do vs (pip install requests)
# invertexto.com/workshopblockchain

import requests

hash = '00000000000000000000c2cc7cddf5b387529a7e2d7149ace58bb202fbac06af'
url = f'https://blockchain.info/rawblock/{hash}'
resposta = requests.get(url)

dados = resposta.json()
print(f'Altura do block: {dados["height"]}')
print(f"Tempo: {dados['time']}")
print(f"Nº de transações: {len(dados['tx'])}")
