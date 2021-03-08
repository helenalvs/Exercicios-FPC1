count = 0
deslocamento = 30
tamanho_botas = list(range(31))
for i in range(len(tamanho_botas)):
    tamanho_botas[i] = [0,0]
N = int(input())
for i in range(N):
    bota = list(input().split())
    numero = int(bota[0])
    if tamanho_botas[numero - deslocamento][0] > 0 and bota[1] == 'E':
        tamanho_botas[numero - deslocamento][0] -= 1
        count += 1
    elif tamanho_botas[numero - deslocamento][1] > 0 and bota[1] == 'D':
        tamanho_botas[numero - deslocamento][1] -= 1
        count += 1
    else:
        if bota[1] == 'D':
            tamanho_botas[numero - deslocamento][0] += 1
        else:
            tamanho_botas[numero - deslocamento][1] += 1
print(count)