somapilhas = 0
tam = int(input())
pilhas = list(map(int, input().split()))
for i in range(len(pilhas)):
    somapilhas += pilhas[i]
somatorio = 0
diferença = 0
a = 0
An = int(((2*somapilhas/tam) + tam-1)/2)
for i in range(tam):
    somatorio += An - i
    if somatorio == somapilhas and i+1 == tam:
        escadaperfeita = list(range(tam))
        for j in range(tam-1, -1, -1):
            escadaperfeita[j] = An - a
            a += 1
        for j in range(tam):
            if pilhas[j] > escadaperfeita[j]:
                diferença += pilhas[j] - escadaperfeita[j]
        print(diferença)
        break
    elif i + 1 == tam:
        print(-1)
        break