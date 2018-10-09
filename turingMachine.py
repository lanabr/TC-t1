from fita import Fita

class TuringMachine:

    def __init__(self, numFitas, estados, alfEntrada, alfFita, transicoes, estadoInicial, estadoFinal):
        # print("Iniciei uma MT")
        # print(numFitas)
        # print(estadoInicial)
        # print(estadoFinal)
        # print(alfEntrada)
        # print(alfFita)
        # print(transicoes)
        self.numFitas = numFitas
        self.estados = estados
        self.alfEntrada = alfEntrada
        self.alfFita = alfFita
        self.transicoes  = transicoes
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
        while self.estadoAtual != self.estadoFinal:
            # FIXME: o estado atual não pode ser uma string
            for t in self.transicoes[int(self.estadoAtual)]:
                pass
        
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
