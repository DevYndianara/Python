# Lista é uma estrutura de dados simples, que permite o armazenamento de elementos (ou nós) sequencialmente. Permite a inserção ou remoção em qualquer de suas posições.


# Varible
cores = ['rosa', 'amarelo', 'preto', 'verde']

#Método 1- inserção: append(x)
cores.append('azul') # o método append insere um item ao fim da lista, equivalente a[len(a):] = [x]

# Método 2 - Inserção em determinada posição da lista: insert(i, x)
cores.insert(3, 'marrom') # o método insert(i, x) insere o item na posíção de índice i e varible x

# Método 3 - Remover item dem uma posição da lista.
#cores.pop() # se estiver com o parêntese vazio, irá remover o último item da lista
#cores.pop(1) # irá remover o item de índice i da lista, informar o número do item.
