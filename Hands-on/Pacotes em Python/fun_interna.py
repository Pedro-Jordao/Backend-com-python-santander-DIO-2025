def principal():
    print ("Função principal executada")

    def interna():
        print ("Função interna executada")

    def funcao_2():
        print ("Função interna 2 executada")

    interna()
    funcao_2()



principal()