# Uso de comandos if - elif - else, se existir mais de uma condição alternativa que precise ser verificada, utilizamos a condição elif, pois, avalia condições antes do comando else

idade = int(input("Digite a idade da pessoa: "))
if idade > 18:
    print("Está grandinho! Passou para o próximo nível  s2")
elif idade > 16:
    print("Sinto muito infanto juvenil! =D")
else:
    print("GAME OVER Menor!!!")