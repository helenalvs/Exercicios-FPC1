total = int(input())
stotal = (total*(total+1))/2
found = list(map(int, input().split()))
soma = 0
for i in range(total-1):
    soma += found[i]
lost = int(stotal-soma)
print(lost)









