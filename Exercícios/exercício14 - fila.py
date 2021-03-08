class No():
    def __init__(self, dado=None):
        self._dado = dado
        self._prox = None
        self._ant = None

    def __str__(self):
        return "{}".format(self._dado)
class Lista():
    def __init__(self):
        self._inicio = None
        self._fim = None

    def isvazia(self):
        if self._inicio == None:
            return True
        else:
            return False

    def inserirnofim(self, dado=None):
        novono = No(dado)
        if self.isvazia() == True:
            self._inicio = self._fim = novono
        else:
            novono._ant = self._fim
            self._fim._prox = novono
            self._fim = novono

    def buscar(self, x):
        i = self._inicio
        while i != None:
            if x == i._dado:
                break
            i = i._prox
        return i

    def remover(self, x):
        noencontrado = self.buscar(x)
        if noencontrado != None:
            if noencontrado._ant != None:
                noencontrado._ant._prox = noencontrado._prox
            else:
                self._inicio = noencontrado._prox
            if noencontrado._prox != None:
                noencontrado._prox._ant = noencontrado._ant
            else:
                self._fim = noencontrado._ant
        return noencontrado

    def __str__(self):
        s = ''
        i = self._inicio
        while i != None:
            s += '{} '.format(str(i))
            i = i._prox
        return s

N = int(input())
fila = list(map(int, input().split()))
M = int(input())
retirados = list(map(int, input().split()))
minhafila = Lista()
for i in fila:
    minhafila.inserirnofim(i)
for i in retirados:
    minhafila.remover(i)
print(minhafila)

