def BuscaBST (raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    else:
        if raiz.chave < chave:
            return BuscaBST(raiz.direita, chave)
        elif raiz.chave > chave:
            return BuscaBST(raiz.esquerda, chave)
        else:
            raiz
            
# Complexidade das operações: 
# Se a árvore binária considerada estiver balanceada, onde ela não irá visitar todas as chaves da árvore - busca: O(log n)
# Se a árvore binária considerada estiver com desbalanceamento progressivo - busca: O(n)
# 
