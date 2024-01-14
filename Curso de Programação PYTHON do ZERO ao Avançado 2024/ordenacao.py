# Ordenar um array do menor para o maior. A função seguinte é para encontrar o menor elemento em um array.

menor = input('Qual o menor valor? ')
menor_indice = input('Qual o índice? ')

def buscaMenor(arr):
    menor = arr[0]  # armazena o menor valor
    menor_indice = 0  # armazena o índice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = 1
    return menor_indice