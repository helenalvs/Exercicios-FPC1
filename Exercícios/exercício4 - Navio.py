def vizinho(tabuleiro, i, j, A, B, idnavio, tam):
    if i<0 or j<0:
        return
    elif i>A or j>B:
        return
    elif tabuleiro[i][j] == '#':
        tam[id] += 1
        tabuleiro[i][j] = idnavio
        vizinho(tabuleiro, i + 1, j, A, B, idnavio, tam)
        vizinho(tabuleiro, i, j + 1, A, B, idnavio, tam)
        vizinho(tabuleiro, i, j - 1, A, B, idnavio, tam)
        vizinho(tabuleiro, i - 1, j, A, B, idnavio, tam)
    else:
        return
def adicionando(A):
    A += [0]

n = list(map(int, input().split()))
index1=n[0]-1
index2=n[1]-1
tabuleiro = list(range(n[0]))
for i in range(n[0]):
    tabuleiro[i] = list(input())
id=0
tam = []
for i in range(n[0]):
    for c in range(n[1]):
        if tabuleiro[i][c] == '#':
            adicionando(tam)
            vizinho(tabuleiro, i, c, index1, index2, id, tam)
            id += 1
#funcionando
tiros = int(input())
alvos = list(range(1, tiros+1))
for i in range(tiros):
    alvos[i] = list(map(int, input().split()))
#número de tiros e a posição dos alvos
t=0
atingidos=0
for i in range(tiros):
    a1, a2 = alvos[i]
    if tabuleiro[a1-1][a2-1] != '.':
        t = tabuleiro[a1-1][a2-1]
        tam[t] += -1
        if tam[t] == 0:
            atingidos+= 1
print(atingidos)
