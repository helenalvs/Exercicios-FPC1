def mergesort(N, p, r, c):
    if p < r:
        q = (p+r)//2
        mergesort(N, p, q, c)
        mergesort(N, q+1, r, c)
        merge(N, p, q, r, c)

def merge(N, p, q, r, c):
    n1 = q - p + 1
    n2 = r - q
    L = list(range(n1))
    R = list(range(n2))
    for i in range(n1):
        L[i] = N[p + i - 1]
    for j in range(n2):
        R[j] = N[q + j]
    i = 0
    j = 0
    k = p-1
    while i < len(L) and j < len(R):
        if L[i][c] >= R[j][c]:
            N[k] = L[i]
            i += 1
        else:
            N[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        N[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        N[k] = R[j]
        j += 1
        k += 1



n = list(map(int, input().split()))
N = list(range(1, n[0]+1))
M = n[1]
med = list(range(M))
for i in range(M):
    med[i] = list(map(int, input().split()))
#print(med)
ouro = 0
prata = 0
bronze = 0
for i in range(n[0]):
    for j in range(M):
        for c in range(3):
            if med[j][c] == N[i]:
                if c == 0:
                    ouro += 1
                elif c == 1:
                    prata += 1
                elif c == 2:
                    bronze += 1
    N[i] = [i, ouro, prata, bronze]
    ouro = 0
    prata = 0
    bronze = 0
p = 1
c = 1
mergesort(N, p, n[0], c)
tam = 1
c = 2
for i in range(n[0]):
    for j in range(i+1, n[0]):
        if N[i][1] == N[j][1]:
            tam += 1
    if tam > 1:
        mergesort(N, i+1, i+tam, c)
    tam = 1
c = 3
for i in range(n[0]):
    for j in range(i+1, n[0]):
        if N[i][1] == N[j][1] and N[i][2] == N[j][2]:
            tam += 1
    if tam>1:
        mergesort(N, i+1, i+tam, c)
    tam = 1
#print(N)
ranking = list(range(1, n[0]+1))
for i in range(n[0]):
    ranking[i] = N[i][0] + 1
for i in range(n[0]):
    print(N[i][0] + 1, end=' ')
#print(N)


