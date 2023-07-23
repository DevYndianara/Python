# Exercício 3.6: Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas
# três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2 e materia3.

materia1 = 5
materia2 = 7
materia3 = 3
media = (materia1 + materia2 + materia3) / 3 # entre parênteses para determinar a prioridade no cálculo

aprovado = media > 7

print(aprovado)

