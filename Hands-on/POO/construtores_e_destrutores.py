class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print ("Iniciando classe....")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo a instância da classe...")


    def falar(self):
            print("auauauauau")

def criar_cachorro():
    c = Cachorro ("Zeus", "branco e preto", False)
    print(c.nome)

c = Cachorro("Rex", "marrom")
c.falar()

print ("Ola mundo")
del c
print("Instância destruída")
c.falar() # Isso causará um erro, pois c foi destruído

criar_cachorro()


