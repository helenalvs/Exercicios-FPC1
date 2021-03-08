def adicionando(A):
    A += [0]
def max(a, b):
    if a >= b:
        return a
    if b > a:
        return b
def canos(matriz, valores, quantidade, limite):
    for i in range(limite+1):
        for j in range(quantidade+1):
            if i != 0 and j != 0:
                if valores[j-1][0] <= i:
                    matriz[i][j] = max(matriz[i][j-1], (matriz[i-valores[j-1][0]][j])+valores[j-1][1])
                elif valores[j-1][0] > i:
                    matriz[i][j] = matriz[i][j-1]
            elif i == 0 or j == 0:
                matriz[i][j] = 0
    return matriz[limite][quantidade]


n = list(map(int, input().split()))
quantidade = n[0]
limite = n[1]
valores = []
for i in range(quantidade):
    adicionando(valores)
    valores[i] = list(map(int, input().split()))
matriz = list(range(limite+1))
for i in range(len(matriz)):
    matriz[i] = list(range(quantidade+1))
k = canos(matriz, valores, quantidade, limite)
print(k)