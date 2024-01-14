cont = [10]

def ImprimearvoreRecurs(raiz, nivel):
    if (raiz == None):
        return nivel + = cont[0]
    
#Imprime Filhos à Direita
    
    ImprimearvoreRecurs(raiz.direita, nivel)
    print()
    
    for i in range(cont[0], nivel):
        print(end=" ")
        print(f"{raiz.chave}<")
        
#Imprime Filhos à Esquerda

ImprimearvoreRecurs(raiz.esquerda, nivel)

def ImprimeArvore(raiz):
    ImprimearvoreRecurs(raiz, 0)