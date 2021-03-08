def descobrir(fazenda, i, j, L, C, sv, sk, id):
    if i <= 0 or j <= 0:
        return
    elif i >= L or j >= C:
        return
    elif fazenda[i][j] == 'v' or fazenda[i][j] == '.' or fazenda[i][j] == 'k':
        if fazenda[i][j] == 'v':
            sv[id] += 1
            fazenda[i][j] = id
        elif fazenda[i][j] == 'k':
            sk[id] += 1
            fazenda[i][j] = id
        elif fazenda[i][j] == '.':
            fazenda[i][j] = id
        descobrir(fazenda, i-1, j, L, C, sv, sk, id)
        descobrir(fazenda, i+1, j, L, C, sv, sk, id)
        descobrir(fazenda, i, j-1, L, C, sv, sk, id)
        descobrir(fazenda, i, j+1, L, C, sv, sk, id)

    else:
        return



n = list(map(int, input().split()))
index1 = n[0]-1
index2 = n[1]-1
fazenda = list(range(n[0]))
for i in range(n[0]):
    fazenda[i] = list(input())

id=0
lobo = 0
ovelha = 0
sv = []
sk = []
for i in range(n[0]):
    for c in range(n[1]):
        if fazenda[i][c] == '.' or fazenda[i][c] == 'v' or fazenda[i][c] == 'k':
            sv.append(0)
            sk.append(0)
            descobrir(fazenda, i, c, index1, index2, sv, sk, id)
            if sv[id] >= sk[id]:
                lobo += sv[id]
                ovelha += 0
            elif sk[id] > sv[id]:
                lobo += 0
                ovelha += sk[id]
            id += 1
print(ovelha, lobo)