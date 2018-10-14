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
        if self.posicao == len(self.fita): #Se atingiu o fim da Fita
            self.fita += [self.branco]

    def movEsquerda(self):
        if self.posicao > 0:
            self.posicao -= 1

    def naoBranco(self):
        if self.fita[self.posicao] == self.branco:
            return False
        else:
            return True

    def __str__(self):
        f = ''.join(self.fita)
        #Enquanto tem simbolos branco no fim da fita os apaga
        while(len(f) > 0 and f[len(f) - 1] == self.branco):
            f = f[:len(f)-1]
        return f
