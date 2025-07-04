class Animal:
    def __init__(self, nro_patas, cor):
        self.nro_patas = nro_patas
        self.cor = cor
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor, nro_patas):
        self.cor = cor
        super().__init__(nro_patas, cor)

class Ave(Animal):
    def __init__(self, cor_bico, nro_patas, cor):
        self.cor_bico = cor_bico
        super().__init__(nro_patas, cor)
    
    # def __str__(self):
    #     return 'ave 42'

class Cachorro (Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornintorinco(Ave, Mamifero):
    def __init__(self, cor_bico, cor, nro_patas):
        # print(Ornintorinco.__mro__) # Método de resolução de ordem, ou seja a ordem de herança e execução dos métodos.

        super().__init__(cor=cor, nro_patas=nro_patas, cor_bico=cor_bico)

cachorro = Cachorro(nro_patas=4, cor="preto")
print(cachorro)

ornintorrinco = Ornintorinco( nro_patas=4, cor_bico="laranja", cor="marrom")

print(ornintorrinco)
