# Cálculo de média semestral, informe a nota do primeiro bimestre e depois do segundo, ao final, irá retornar com a média e se foi aprovado ou reprovado

print('=====>  NOTAS DO PRIMEIRO SEMESTRE  <=====')
print()
n1 = float(input(f"|   Digite a nota do primeiro bimestre:  " )) #necessario inserir o f para determinar o print do tipo str
n2 = float(input("|   Digite a nota do segundo bimestre:  "))
print()
print('=====>------------------------------<=====')

#Orientação sobre as máscaras:
# %d - nº inteiros / %s - strings / %f - nº decimais / "%3d" % x - nesse caso, o nº int irá ocupar três posições e o que está após % será acrescentado no lugar do valor que está sendo determinado a ser impresso. / {} - usada para determinar a máscara a ser impressa, adicionando dois pontos e um nº {:3}, ele substitui o uso de %d, %s, %f. 

#Calcular a média
mfinal = (n1 + n2) / 2

#Verificação
if mfinal >= 7.0:
    print()
    print("=====>       RESULTADO FINAL      <=====")
    print("|   A Média: %.1f - Aprovado   \o/ "% mfinal)
    print()
    print('=====>----------------------------<=====')
else:
    print()
    print("=====>       RESULTADO FINAL      <=====")
    print("|   A Média: %.1f - Reprovado   "% mfinal)
    print()
    print('=====>----------------------------<=====')
    