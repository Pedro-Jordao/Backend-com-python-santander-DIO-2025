"""
class Estudante:
    escola = "FIAP"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"nome={self.nome}, matricula={self.matricula}, escola={self.escola}"

def mostra_valores(*args):
    for arg in args:
        print(arg)

aluno1 = Estudante("João", 12345)
aluno2 = Estudante("Maria", 67890)
mostra_valores(aluno1, aluno2)

aluno1.matricula = 2
mostra_valores("\n", aluno1, aluno2)

Estudante.escola = "Senac Lapa Tito"
aluno3 = Estudante("Pedro", 11223)
mostra_valores("\n", aluno1, aluno2, aluno3)
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade=idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

def mostra_valores(*args):
    for arg in args:
        print(arg)

pessoa1 = Pessoa("João", 30)
mostra_valores(pessoa1)
 