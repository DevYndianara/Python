# Podemos usar valores individuais de uma lista, como faríamos com qlquer variável. Pode usar f-strings para criar mensagens com base em um valor de uma lista.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)