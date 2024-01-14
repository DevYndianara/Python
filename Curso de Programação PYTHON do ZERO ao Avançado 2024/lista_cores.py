# Listas:
# Arnazenar mais de uma informacao em variaveis
# Manter a sequencia dos dados em uma variavel

cor_escolhida = input('Digite a cor desejada: ')
cores = ['rosa', 'lilas', 'preto', 'verde']

if cor_escolhida.lower() in cores: #o lower configura o programa para que leia fonte em cx alta ou baixa
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')