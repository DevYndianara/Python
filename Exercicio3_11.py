#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

price = int(input("Digite o valor da mercadoria: "))
porcentagem = int(input("Digite o percentual de desconto: "))
discount = price * porcentagem / 100

print(f"O valor do desconto foi de R$ {discount:5.2f},"f" o preço a pagar é de R$ {price - discount:5.2f}")