from turingMachine import TuringMachine

numFitas = input()
numEstados, tamAlfEntrada, tamAlfFita, numTransicoes = [int(i.strip()) for i in input().strip().split(' ')]
estados = input()
alfEntrada = input()
alfFita = input()

transicoes = []

for i in range(numTransicoes):
    transicoes.append(input())

entrada = input()

print(numFitas)
print(numEstados)
print(tamAlfEntrada)
print(tamAlfFita)
print(numTransicoes)
print(estados) #pegar o final e o inicial como o último e o primeiro
print(alfEntrada)
print(alfFita)
print(transicoes)
print(entrada)
