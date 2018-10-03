class Fita:
    #Define a fita: sequencia de simbolos, posição na fita onde o cabeçote aponta
    def __init__(self, fita = [], branco = ' '):
        self.fita = [branco]
        self.posicao = 0
        self.branco = branco

    #Leitura na fita: lẽ o símbolo onde o cabeçote aponta
    def lerFita(self):
        return self.fita[self.posicao]

    #Escrita na fita: escreve no local onde o cabeçote aponta
    def escreverFita(self, char):
        self.fita[self.posicao] = char

    def movDireita(self):
        self.posicao += 1

    def movEsquerda():
        self.posicao -= 1
