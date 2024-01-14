# Para buscar a posição do item na lista, utilize o método index(x), sendo i a varible.
  # cod. de busca: usando index (x);
  # implementando a busca;
  # Complexidade O (n), pois, precisará percorrer toda a lista
  
# Varible
cores = ['rosa', 'amarelo', 'preto', 'verde']
i = cores.index('preto') # o index irá printar a posição do item armazenado
print(i)

# Busca do item da lista armazenada em L
def buscaLista(k, L, n):
    i = 0
    indiceL = -1
    while i < n: #enquanto não chegar ao final da lista
        if L[i] == k: # se o item da lista corresponder ao campo de busca k
            indiceL = i # irá retornar esse código do nó encontrado
            i = n + 1
        i = i + 1 # senão encontrar, irá avançar mais um item na lista e volta para o início da estrutra de repetição while
    return indiceL