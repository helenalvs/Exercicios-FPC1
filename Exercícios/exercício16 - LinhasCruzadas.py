count = 0
def mergeSort(pontos):
    global count
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
                count += len(inicio) - i
            k += 1
        while i < len(inicio):
            pontos[k] = inicio[i]
            i += 1
            k += 1
        while j < len(fim):
            pontos[k] = fim[j]
            j += 1
            k += 1

N = input()
pontos = list(map(int, input().split()))
mergeSort(pontos, count)
print(count)