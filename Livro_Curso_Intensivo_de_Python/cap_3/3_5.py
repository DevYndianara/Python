# Mudando a lista de convidados: você acabou  de ficar sabendo que um dos convidados não conseguirá ir ao jantar, assim precisa enviar um conjunto novo de convites. É necessário convidar outra pessoa.
# * Comente com o programa do exercícios 3.4. No final do programa, adicione um print(), informando o nome do convidado que não irá ao jantar.
# * Modifique sua lista substituido o nome do convidado que não pode comparecer pelo nome da pessoa nova que você está convidando.
# * Exiba um segundo conjunto de mensagens de convite, uma para cada pessoa que ainda não consta em sua lista.

convidados = ['fulano', 'cicrano', 'beltrano']
naoira_owned = convidados.pop(0)
felizardo_owned = convidados.pop(1)
print(f"Nesse jantar, o {naoira_owned.title()} não poderá comparecer e {felizardo_owned.title()} irá.")