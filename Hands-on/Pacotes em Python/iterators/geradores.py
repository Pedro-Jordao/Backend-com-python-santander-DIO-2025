"""
Um gerador é uma forma especial de iterador em Python, que permite criar iteradores de forma mais simples e concisa.
Os geradores são definidos usando funções normais, mas em vez de usar a palavra-chave `return`, utilizam a palavra-chave `yield`.
Quando a função é chamada, ela retorna um objeto gerador, mas a execução da função é pausada até que o próximo elemento seja solicitado.
"""
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3, 4, 5]):
    print(i)