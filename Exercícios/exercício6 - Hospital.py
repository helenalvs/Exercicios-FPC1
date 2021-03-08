def enumerando(fila, i):
    fila[i][2] = int(fila[i][2])
    if fila[i][1] == 'premium':
       fila[i][1] = int(6)
    elif fila[i][1] == 'diamante':
        fila[i][1] = int(5)
    elif fila[i][1] == 'ouro':
        fila[i][1] = int(4)
    elif fila[i][1] == 'prata':
        fila[i][1] = int(3)
    elif fila[i][1] == 'bronze':
        fila[i][1] = int(2)
    elif fila[i][1] == 'resto':
        fila[i][1] = int(1)

def mergesort(fila, p, r, c):
    if p < r:
        q = (p+r)//2
        mergesort(fila, p, q, c)
        mergesort(fila, q+1, r, c)
        merge(fila, p, q, r, c)

def merge(fila, p, q, r, c):
    n1 = q - p + 1
    n2 = r - q
    L = list(range(n1))
    R = list(range(n2))
    for i in range(n1):
        L[i] = fila[p + i - 1]
    for j in range(n2):
        R[j] = fila[q + j]
    i = 0
    j = 0
    k = p-1
    if c>0:
        while i < len(L) and j < len(R):
            if L[i][c] >= R[j][c]:
                fila[k] = L[i]
                i = i + 1
            else:
                fila[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            fila[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            fila[k] = R[j]
            j = j + 1
            k = k + 1
    else:
        while i < len(L) and j < len(R):
            if L[i][c] < R[j][c]:
                fila[k] = L[i]
                i = i + 1
            else:
                fila[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            fila[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            fila[k] = R[j]
            j = j + 1
            k = k + 1


npacientes = int(input())
fila = list(range(npacientes))
for i in range(npacientes):
    fila[i] = list(input().split())
    enumerando(fila, i)
p = 1
c=1
mergesort(fila, p, npacientes, c)
c=2
tam = 1
for i in range(0, npacientes):
    for j in range(i+1, npacientes):
        if fila[i][1] == fila[j][1]:
            tam += 1
    if tam > 1:
        mergesort(fila, i+1, i+tam, c)
    tam = 1
tam = 1
c = 0
for i in range(0, npacientes):
    for j in range(i+1, npacientes):
        if fila[i][1] == fila[j][1] and fila[i][2] == fila[j][2]:
            tam = tam + 1
    if tam > 1:
        mergesort(fila, i+1, i+tam, c)
    tam = 1
for j in range(npacientes):
    print(fila[j][0])

