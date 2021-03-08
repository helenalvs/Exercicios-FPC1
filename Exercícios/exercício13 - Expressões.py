class No():
    def __init__(self, dado=None):
        self._dado = dado
        self._prox = None
        self._ant = None

    def __str__(self):
        return "{}".format(self._dado)
class Pilha(No):
    def __init__(self):
        self._inicio = None
        self._fim = None
    def isvazia(self):
        if self._inicio == None:
            return True
        else:
            return False
    def push(self, dado=None):
        novono = No(dado)
        if self.isvazia():
            self.fim = novono
        else:
            novono._prox = self._inicio
            self._inicio._ant = novono
        self._inicio = novono
    def pop(self):
        if not self.isvazia():
            if self._inicio._prox == None:
                self._fim = None
            else:
                self._inicio._prox._ant = None
            self._inicio = self._inicio._prox
    def buscarPrimeiro(self):
        return str(self._inicio)


num = int(input())
for i in range(num):
    expressoes = list(input())
    if len(expressoes) % 2 == 0:
        minhapilha = Pilha()
        for j in range(len(expressoes)):
            if expressoes[j] == '[' or expressoes[j] == '(' or expressoes[j] == '{':
                minhapilha.push(expressoes[j])
            elif expressoes[j] == ']' and minhapilha.buscarPrimeiro() == '[':
                minhapilha.pop()
            elif expressoes[j] == ')' and minhapilha.buscarPrimeiro() == '(':
                minhapilha.pop()
            elif expressoes[j] == '}' and minhapilha.buscarPrimeiro() == '{':
                minhapilha.pop()
            else:
                minhapilha.push(expressoes[j])
                break
        if minhapilha.isvazia():
            print('S')
        else:
            print('N')
    else:
        print('N')
