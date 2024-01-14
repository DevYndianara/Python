def InserirBST(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    else:
        if raiz.chave == chave:
            return raiz
        elif raiz.chave < chave:
            raiz.direita = InserirBST(raiz.direita, chave)
        else:
            raiz.esquerda = InserirBST(raiz.esquerda, chave)
    return raiz