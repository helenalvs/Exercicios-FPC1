count = 0
def mergeSort(pontos):
    if len(pontos) > 1:
        meio = len(pontos) // 2
        inicio = pontos[:meio]
        fim = pontos[meio:]

        mergeSort(inicio)
        mergeSort(fim)

        i = j = k = 0

        while i < len(inicio) and j < len(fim):
            if inicio[i] < fim[j]:
                pontos[k] = inicio[i]
                i += 1
            else:
                pontos[k] = fim[j]
                j += 1
            k += 1
        while i < len(inicio):
            pontos[k] = inicio[i]
            i += 1
            k += 1
        while j < len(fim):
            pontos[k] = fim[j]
            j += 1
            k += 1


N = list(map(int, input().split()))
bytes = N[1]
numArquivos = N[0]
arquivos = list(map(int, input().split()))
mergeSort(arquivos)
i = 0
j = len(arquivos)-1
while i <= j:
    if arquivos[i] + arquivos[j] <= bytes:
        i += 1
        j -= 1
        count += 1
    elif arquivos[j] <= bytes:
        j -= 1
        count += 1
print(count)
