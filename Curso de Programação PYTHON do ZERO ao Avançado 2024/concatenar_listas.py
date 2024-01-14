# Listas:
# Arnazenar mais de uma informacao em variaveis
# Manter a sequencia dos dados em uma variavel

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20,30,40,50]

duas_listas = zip(cores, valores) # o comando zip junta as duas listas e cria duas tuplas
print(list(duas_listas)) # a função list imprime o resultado das tuplas