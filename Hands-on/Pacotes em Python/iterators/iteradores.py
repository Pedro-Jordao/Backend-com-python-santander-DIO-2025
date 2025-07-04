"""
Um iterador é um objeto que implementa o protocolo de iteração em Python, permitindo percorrer uma coleção de elementos,
como listas, tuplas ou dicionários, sem precisar conhecer a estrutura interna desses objetos.
Um iterador é um objeto que implementa os métodos `__iter__()` e `__next__()`. O método `__iter__()` retorna o próprio iterador,
enquanto o método `__next__()` retorna o próximo elemento da coleção. Quando não há mais elementos, `__next__()` deve lançar a
exceção `StopIteration`.
"""
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self): # O método __iter__ deve retornar o próprio iterador, que é a instância da classe.
        return self
    def __next__(self): # O método __next__ deve retornar o próximo elemento da coleção. 
        try:
            numero =  self.numeros[self.contador] 
            self.contador += 1
            return numero * 2
        except: # Se não houver mais elementos, lança StopIteration. A exceção pode ser mais específica, com IndexError, que é o erro que aconteceria.
            raise StopIteration


for i in MeuIterador(numeros=[1, 2, 3, 4, 5]):
    print(i)