# def meu_gerador():
#     yield 1

# for i in meu_gerador():
#     print(i)

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3, 4, 5]):
    print(i)

"""
Em termos gerais, você utilizará um gerador quando o código for simples e você quiser criar um iterador de forma rápida e fácil
além de o gerador ser mais eficiente em termos de memória.

Você utilizará um iterador quando precisar de mais controle sobre o processo de iteração, como quando precisar manter o 
estado entre as iterações.

"""