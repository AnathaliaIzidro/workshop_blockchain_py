from bit import Key

key = Key()

# Como criar uma carteira?
wallet = key.address
print(f'Minha wallet: {wallet}')

#Abrir o terminal do VS e digitar (pip install bit)

# Como vizualizar o saldo da carteira
saldo = key.get_balance()
print(f'Meu saldo: {saldo}')