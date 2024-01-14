# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, integer, float, boolean...

aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota_final': 'A', 
    'ap': True, 
    'Materias': ['Fisica', 'Matematica', 'Filosofia']
}

#for x in aluno: # imprime as keys e não os valores
#    print(x)

#for x in aluno.values(): # nesse caso, a função está solicitando os valores
#    print(x)

#for keys, values in aluno.items():# a função está chamando das keys e values os itens de cada
#    print(keys, values)

# print(aluno.get('Materias'))
# print(len(aluno)) # o comando len retorna a quantidade de itens

print(aluno.items()) # retorna os itens do dicionário
print(aluno.keys()) # retorna as chaves do dicionário
print(aluno.values())

