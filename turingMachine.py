from fita import Fita

class TuringMachine:

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
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal

    def run(self, fitasEntrada):
        print("RUN")
        print(fitasEntrada)

        #Ajusta a nova fita
        self.limpaFita()
        for i in fitasEntrada:
            self.fitas[0].escreverFita(i)
            self.fitas[0].movDireita()

        self.fitas[0].posicao = 0
        self.posicao = self.estadoInicial

    def limpaFita(self):
        self.fitas = []
        for i in range(self.numFitas):
            self.fitas += [Fita(branco = self.alfFita[len(self.alfFita) - 1])]
