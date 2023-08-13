#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Informe o valor do salário: "))
porcentagem = float(input("Qual a porcentagem de aumento? "))
aumento = salario * porcentagem / 100

print(f"O aumento foi de R$ {aumento:5.2f}", f"totalizando em R$ {salario+aumento:5.2f}")