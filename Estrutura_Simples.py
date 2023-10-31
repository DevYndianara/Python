# A estrutura simples utiliza a condição if, avaliando se o resultado for verdadeiro executará uma determinada ação dentro dos padrões determinados na condição.

A = input("Informe um valor para a variável A: ")
B = input("Informe um valor para a variável B: ")

if (A > B):
    aux = A;
    A = B;
    B = aux;

print("O valor da variável A agora é : ", A);
print("O valor da variável B agora é : ", B);