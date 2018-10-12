from fita import Fita

class TuringMachine:
    transEntrada = [] 
    transSaida = []
    def __init__(self, numFitas, estados, alfEntrada, alfFita, transicoes, estadoInicial, estadoFinal):
        print("Iniciei uma MT")
        print(numFitas)
        print(estadoInicial)
        print(estadoFinal)
        print(alfEntrada)
        print(alfFita)
        print(transicoes)
        self.numFitas = numFitas
        self.estados = estados
        self.alfEntrada = alfEntrada
        self.alfFita = alfFita
        self.transicoes  = transicoes
        self.traduzTransicao()
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.estadoAtual = estadoInicial

    def run(self, w):
        print("Entrada W:")
        print(w)

        #Ajusta a nova fita criando Nfitas em branco
        self.limpaFita()
        #Escreve a entrada na primeira fita
        for i in w:
            self.fitas[0].escreverFita(i)
            self.fitas[0].movDireita()

        for i in range(self.numFitas):
            print("Fita %d antes:" % i)
            print(self.fitas[i])

        self.fitas[0].posicao = 0
        self.posicao = self.estadoInicial

        #Verifica a fita de entrada:
        for s in w:
            # if s not in self.alfFita:
            if self.alfFita.count(s) == 0:
                self.estadoAtual = 'entrada invalida'
                self.mostraSaida()
                return

        #Execução das transições fazendo as marcações:
        #AQUI FAZER ##################################

        valida = True
        #procurando a transição correta
        for d, i in enumerate(self.transEntrada):
            #se o estadoAtual é igual ao estado da transição
            if(i[0] == self.estadoAtual):
                #para cada fita verifica se os simbolos são os da transição
                for c, f in enumerate(self.fitas):
                    #se algum for diferente, não é a transição correta
                    if (f.lerFita() != i[1][c]):
                        valida = False
                #se a transição correta foi encontrada
                if(valida == True):
                    #o novo estado é o estado da transição
                    self.estadoAtual = self.transSaida[d][0]
                    #pra cada fita, escreve por cima da posição do cabeçote, e move(ou n)
                    for e, f in enumerate(self.fitas):
                        f.escreverFita(self.transSaida[d][1][e])
                        if(self.transSaida[d][2][e] in ['R','D']):
                            f.movDireita()
                        elif(self.transSaida[d][2][e] in ['L', 'E'] ):
                            f.movEsquerda()
            #se a transição ocorreu, para o laço que procura transição
            if(valida == True):
                break
        for i in range(self.numFitas):
            print("Fita %d antes:" % i)
            print(self.fitas[i])


                        


        self.mostraSaida()

    def mostraSaida(self):

        print("Fita depois pós marcações:")
        print(self.fitas[0])

        if self.estadoAtual == 'entrada invalida':
            print("Rejeita")
            return

        if self.estadoAtual != self.estadoFinal:
            print("Rejeita")
        else:
            print(self.fitas[0])

    #Limpa as fitas, colocando brancos
    def limpaFita(self):
        self.fitas = []
        for i in range(self.numFitas):
            self.fitas += [Fita(branco = self.alfFita[len(self.alfFita) - 1])]
            # self.fitas.append(Fita(branco = self.alfFita[-1]))
        
    def traduzTransicao(self):
        for t in self.transicoes:
            Entrada, Saida = t.split("=")
            Entrada = Entrada.strip("()").split(",")
            Saida = Saida.strip("()").split(",")
            self.transEntrada.append(Entrada)
            self.transSaida.append(Saida)
