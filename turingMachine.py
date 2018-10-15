from fita import Fita
import sys


class TuringMachine:
    #transições 
    transEntrada = []
    transSaida = []

    #Inicia uma MT
    def __init__(self, numFitas, numTransicoes, estados, alfEntrada, alfFita, transicoes, estadoInicial, estadoFinal):
        print("Iniciei uma MT:\n")
        print("Numero de fitas = ", numFitas)
        print("Estado inicial = ", estadoInicial)
        print("Estado final = ", estadoFinal)
        print("Alfabeto de entrada = ", alfEntrada)
        print("Alfabeto da fita = ", alfFita)
        print("Transições = ", transicoes)
        print("\n\n")
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

    #Executa uma MT
    def run(self, w):
        print("Entrada W =", w)
        
        #Ajusta a nova fita criando Nfitas em branco
        self.limpaFita()
        #Escreve a entrada na primeira fita
        for i in w:
            self.fitas[0].escreverFita(i)
            self.fitas[0].movDireita()

        for i in range(self.numFitas):
            print("Fita %d antes =" % i, self.fitas[i])
        
        #Setando o cabeçote e o estado inicial
        self.fitas[0].posicao = 0
        self.posicao = self.estadoInicial

        #Verifica se a fita de entrada é válida:
        for s in w:
            # Se s não estiver no alfabeto da fita:
            if self.alfFita.count(s) == 0:
                self.estadoAtual = 'entrada invalida'
                self.mostraSaida()
                return

        c = 0
        #percorre toda a entrada simbolo a simbolo
        while (self.estadoAtual != self.estadoFinal):
            achou = False
            #print("\nsimbolo: %s" % c)
            #Para o simbolo atual, verifica se alguma transição a satisfaz considerando o estado atual da fita e a posição dos cabeçotes
            for d in range(self.numTransicoes):
                if(achou):#se já achou uma transição sai do for
                    break
                valida = True
                print("\nTransição: %s %s \nEstado atual: %s " % (self.transEntrada[d], self.transSaida[d], self.estadoAtual))
                if(self.transEntrada[d][0] == self.estadoAtual): #Se o estado atual é o mesmo estado da proxima transição, verifica ela
                    for c, f in enumerate(self.fitas): #Para todas as fitas
                        print("fita", c, "=",f.lerFita())
                        if(f.lerFita() != self.transEntrada[d][1][c]): #Se o simbolo lido na transição é diferente do simbolo da fita, vai pra proxima transição
                            print("transicao errada!")
                            valida = False
                            break
                    #Se encontra transição
                    if(valida == True):
                        print("encontrou transicao valida!")
                        achou = True
                        #Estado atual é atualizado
                        self.estadoAtual = self.transSaida[d][0]
                        print("\n\nEstado novo: %s" % self.estadoAtual)
                        #As fitas são atualizadas e o cabeçote é movido
                        for e, f in enumerate(self.fitas):
                            f.escreverFita(self.transSaida[d][1][e])
                            if(self.transSaida[d][2][e] in ['R','D']):
                                f.movDireita()
                            elif(self.transSaida[d][2][e] in ['L', 'E'] ):
                                f.movEsquerda()
                else:
                    print("transição errada!")
                                
            #Não achou nenhuma transição para seguir com os simbolos atuais no estado atual. Rejeita
            if((achou == False) & (self.estadoAtual != self.estadoFinal)):
                self.estadoAtual = 'entrada invalida'
                self.mostraSaida()
                return
            c+=1
            if c == 50:
                break

        self.mostraSaida()

    def mostraSaida(self):

        print("\nFitas após marcações:")
        for i in range(self.numFitas):
            print("Fita %d =" % i, self.fitas[i])

        if self.estadoAtual == 'entrada invalida':
            print("Rejeita")
            return

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
