def adicionando(A):
    A += [0]
def maior_digito(n, L, R):
    chave = n[L]
    index = L
    if L == R:
        index = L
    else:
        for i in range(L, R):
            if chave < n[i+1]:
                chave = n[i+1]
                index = i + 1
    return index

quant = []
num = []
i = 0
while True:
    try:
        adicionando(quant)
        quant[i] = list(map(int, input().split()))
        if quant[i]:
            adicionando(num)
            num[i] = list(map(int, input().strip()))
            i += 1
        else:
            break
    except EOFError or ValueError:
        break
a = 0
for i in range(len(num)):
    limite = quant[i][1]
    indice = 0
    for j in range(quant[i][0] - quant[i][1]):
        R = limite
        indice = maior_digito(num[i], indice, R)
        if j+1 == quant[i][0] - quant[i][1]:
            print(num[i][indice])
        else:
            print(num[i][indice], end='')
        indice += 1
        limite += 1