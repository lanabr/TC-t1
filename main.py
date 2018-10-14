from turingMachine import TuringMachine
from fita import Fita

#Leitura do arquivo:
numFitas = int(input())
numEstados, tamAlfEntrada, tamAlfFita, numTransicoes = [int(i.strip()) for i in input().strip().split(' ')]
estados = input().strip().split(' ')
estadoInicial = estados[0]
estadoFinal = estados[numEstados-1]
alfEntrada = input()
alfFita = input()
transicoes = []

for i in range(numTransicoes):
    transicoes.append(input())

#Le a entrada w
w = input()
#Inicio Máquina de Turing
mt = TuringMachine(numFitas, numTransicoes, estados, alfEntrada, alfFita, transicoes, estadoInicial, estadoFinal)
mt.run(w)
