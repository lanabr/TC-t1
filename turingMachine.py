from fita import Fita
import sys

class TuringMachine:
    transEntrada = []
    transSaida = []
    def __init__(self, numFitas, numTransicoes, estados, alfEntrada, alfFita, transicoes, estadoInicial, estadoFinal):
        print("Iniciei uma MT")
        print(numFitas)
        print(estadoInicial)
        print(estadoFinal)
        print(alfEntrada)
        print(alfFita)
        print(transicoes)
        self.numFitas = numFitas
        self.numTransicoes = numTransicoes
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

        for i in range(self.numTransicoes):
            print(self.transicoes[i])

        # print("Transicao de entrada:")
        # print(self.transEntrada)
        #
        # print("Transicao de saída:")
        # print(self.transSaida)

        c = 0
        
        while (c < len(w)): #percorre toda a entrada simbolo a simbolo
            achou = False
            print("\nsimbolo: %s" % c)
            #Para o simbolo atual, verifica se alguma transição a satisfaz considerando o estado atual da fita e a posição dos cabeçotes
            for d in range(self.numTransicoes):
                if(achou):#se já achou uma transição sai do for
                    break
                valida = True
                print("Estado atual: %s \nTransição: %s %s" % (self.estadoAtual, self.transEntrada[d], self.transSaida[d]))
                if(self.transEntrada[d][0] == self.estadoAtual): #Se o estado atual é o mesmo estado da proxima transição, verifica ela
                    for c, f in enumerate(self.fitas): #Para todas as fitas
                        if(f.lerFita() != self.transEntrada[d][1][c]): #Se o simbolo lido na transição é diferente do simbolo da fita, vai pra proxima transição
                            print("%s != %s" % (f.lerFita(), self.transEntrada[d][1][c]))
                            valida = False
                            break
                        else:
                            print("%s == %s" % (f.lerFita(), self.transEntrada[d][1][c]))

                    if(valida == True):
                        achou = True
                        self.estadoAtual = self.transSaida[d][0]
                        print("Estado novo: %s" % self.estadoAtual)
                        for e, f in enumerate(self.fitas):
                            f.escreverFita(self.transSaida[d][1][e])
                            if(self.transSaida[d][2][e] in ['R','D']):
                                f.movDireita()
                            elif(self.transSaida[d][2][e] in ['L', 'E'] ):
                                f.movEsquerda()
            c+=1

        self.mostraSaida()

    def mostraSaida(self):

        print("Fitas após marcações:")
        for i in range(self.numFitas):
            print(self.fitas[i])

        if self.estadoAtual == self.estadoFinal:
            print("Aceita")
            return
        elif self.estadoAtual != self.estadoFinal:
            print("Rejeita")

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
