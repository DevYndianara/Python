# Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de conhecer:
#   Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética;
#   Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente; basta exibi-la como uma lista crua do Python.
#   User sorted() para exibir sua lista em ordem alfabética, sem alterar a lista original.
#   Mostre que sua lista ainda está na ordem original exibindo-a;
#   Use o sorted() para exibir sua lista em ordem alfabética reversa, sem alterar a ordem original dela.
#   Demonstre que sua lista ainda está na ordem original exibindo-a mais uma vez.
#   Use o reverse() para alterar a ordem de sua lista. Exiba essa lista para mostrar que sua ordem foi alterada.
#   Use o reverse() para alterar a ordem de sua lista novamente. Exiba-a a fim de mostrar que voltou a ordem original.
#   Use o sort() para alterar sua lista para que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem foi alterada.
#   Use sort() para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem foi alterada.

locais = ['lençóis maranhenses', 'foz do iguaçu', 'machu picchu']
print(locais)

print(sorted(locais))

print(locais)

locais.reverse()
print(locais)

locais.reverse()
print(locais)

locais.sort()
print(locais)

locais.sort(reverse=True)
print(locais)