class No():
    def __init__(self, dado=None):
        self.dado = str(dado)
        self.prox = None
        self.ant = None

    def __str__(self):
        return "{}".format(self.dado)

class Lista():
    def __init__(self):
        self.inicio = None
        self.fim = None

    def isvazia(self):
        if self.inicio == None:
            return True
        else:
            return False

    def inserirnofim(self, dado=None):
        novono = No(dado)
        if self.isvazia() == True:
            self.inicio = self.fim = novono
        else:
            novono.ant = self.fim
            self.fim.prox = novono
            self.fim = novono

    def buscar(self, x):
        i = self.inicio
        while i != None:
            if x == i.dado:
                break
            i = i.prox
        return i

    def remover(self, x):
        noencontrado = self.buscar(x)
        if noencontrado != None:
            if noencontrado.ant != None:
                noencontrado.ant.prox = noencontrado.prox
            else:
                self.inicio = noencontrado.prox
            if noencontrado.prox != None:
                noencontrado.prox.ant = noencontrado.ant
            else:
                self.fim = noencontrado.ant
        return noencontrado

    def __str__(self):
        s = ''
        i = self.inicio
        while i != None:
            s += '{} '.format(str(i))
            i = i.prox
        return s
class Fila(Lista):
    def removerDoInicio(self):
        if not self.isvazia():
            if self.inicio.prox == None:
                self.fim = None
            else:
                self.inicio.prox._ant = None
            self.inicio = self.inicio.prox
    def comparando(self, x):
        i = self.inicio
        j = x.inicio
        if str(i) == str(j):
            x.removerDoInicio()
        else:
            if x.inicio.prox != None:
                x.inserirnofim(j)
                x.removerDoInicio()

F = int(input())
deckconvidados = []
for i in range(F):
    deckMesa = list(map(int, input().split()))
    listatemporária = deckMesa
    deckMesa = Fila()
    for i in listatemporária:
        deckMesa.inserirnofim(i)
    numJogadores = 0
    while True:
        k = list(map(int, input().split()))
        if k[0] != -1:
            deckconvidados.append(Fila())
            for i in k:
                deckconvidados[-1].inserirnofim(i)
            numJogadores += 1
        else:
            break
    j = True #para rodar o while
    totRodadas = 0 #para contar as rodadas
    while j == True:
        totRodadas += 1
        if totRodadas == 1000:
            print(0)
            break
        for i in range(numJogadores):
            deckMesa.comparando(deckconvidados[i])
            if deckconvidados[i].isvazia()==True:
                print(i+1)
                j = False
                break
        deckMesa.inserirnofim(deckMesa.inicio)
        deckMesa.removerDoInicio()
    deckMesa = []
    deckconvidados = []
