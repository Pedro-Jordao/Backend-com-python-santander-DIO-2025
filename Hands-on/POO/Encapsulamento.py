# class Conta:
#     def __init__(self, nro_agencia,saldo=0):
#         self._saldo = saldo
#         self.nro_agencia = nro_agencia

#     def depositar(self, valor):
#         # ...
#         self._saldo += valor

#     def sacar(self, valor):
#         # ...
#         self._saldo -= valor
    
#     def mostrar_saldo(self):
#         return self._saldo



# conta = Conta("001", 100)
# conta.depositar(50)
# # print(conta._saldo)  # Atributo protegido por convenção, mas acessível
# print(conta.nro_agencia)  # Atributo público, acessível diretamente

# print(conta.mostrar_saldo())  # Método público para acessar o saldo


###############################################################################


"""
Propriedades (property()) são uma maneira de encapsular o acesso a
atributos de uma classe, permitindo que você controle como os valores
são obtidos e definidos. Elas são úteis para validar dados ou para calcular
valores dinamicamente.
"""






"""
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    @x.setter
    def x(self, value):
        self._x += value
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)  # Acessa o valor de x através do getter
foo.x = 10
print(foo.x)  # Acessa o valor atualizado de x através do getter

del foo.x  # Deleta o atributo x, chamando o deleter

print (foo.x)  # Acessa o valor de x após a deleção, que agora é -1


"""

import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = datetime.datetime.now().year
        return _ano_atual - self._ano_nascimento



pessoa = Pessoa("João", 1990)
print(f"Nome da pessoa: {pessoa.nome} - Idade: {pessoa.idade} anos")