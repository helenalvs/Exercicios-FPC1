def adicionando(A):
    A += [0]
def min(a, b, c):
    if a <= b and a <= c:
        return a
    if b < a and b <= c:
        return b
    if c < a and c < b:
        return c

def max(a, b, c):
    if a >= b and a >= c:
        return a
    if b > a and b >= c:
        return b
    if c > a and c > b:
        return c

def edição(matriz, S, T):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if j != 0 and i != 0:
                    if S[i-1] != T[j-1]:
                        matriz[i][j] = min(matriz[i][j-1], matriz[i-1][j-1], matriz[i-1][j]) + 1
                    if S[i-1] == T[j-1]:
                        matriz[i][j] = matriz[i-1][j-1]
                if j == 0:
                    matriz[i][j] = i
                if i == 0:
                    matriz[i][j] = j
        return matriz[len(matriz)-1][len(matriz[0])-1]


tam = list(map(int, input().split()))
n = tam[0]
m = tam[1]
dicionario = []
palavras = []
for i in range(n):
    adicionando(dicionario)
    dicionario[i] = list(input())
for j in range(m):
    adicionando(palavras)
    palavras[j] = list(input())
j = 0
corrigido = list(range(m))
for i in range(len(corrigido)):
    corrigido[i] = list(range(n))
for i in range(m):
    while j < n:
        matriz = list(range(len(dicionario[j]) + 1))
        for c in range(len(dicionario[j]) + 1):
            matriz[c] = list(range(len(palavras[i]) + 1))
        k = edição(matriz, dicionario[j], palavras[i])
        if k <= 2:
            corrigido[i][j] = dicionario[j]
            j += 1
        else:
            corrigido[i][j] = 0
            j += 1
    j = 0

for i in range(len(corrigido)):
    for j in range(len(corrigido[i])):
        if corrigido[i][j] != 0:
            for c in range(len(corrigido[i][j])):
                if c+1 == len(corrigido[i][j]):
                    print(corrigido[i][j][c], end=' ')
                else:
                    print(corrigido[i][j][c], end='')
    print('')
