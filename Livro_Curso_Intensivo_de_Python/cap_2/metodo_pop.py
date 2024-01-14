# O método pop() remove o último elemento de uma lista, mas possibilita que você trabalhe com esse elemento após removê-lo. O termo pop se origina da ideia de considerar uma lista como uma pilha de itens, removendo um item do topo da pilha. Analogicamente, o topo de uma pilha corresponde ao final de uma lista.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)