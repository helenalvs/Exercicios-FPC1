def sucessor(a):
    return a + 1

def soma(a,b):
    for i in range(b):
       a = sucessor(a)
    return a

def mult(a,b):
    c = 0
    for i in range(b):
        c = soma(c,a)
    return c
def exp(a,b):
    c = 1
    for i in range (b):
        c = mult(c,a)
    return c

while True:
    entrada = input()
    if entrada:
        entrada = entrada.split()
        if entrada[0] == "Suc":
            print(sucessor(int(entrada[1])))
        elif entrada[0] == "Soma":
            print(soma(int(entrada[1]), int(entrada[2])))
        elif entrada[0] == "Mult":
            print(mult(int(entrada[1]), int(entrada[2])))
        elif entrada[0] == "Exp":
            print(exp(int(entrada[1]), int(entrada[2])))
    else:
        break





#A = int(input("Informe o primeiro número: "))
#B = int(input("Informe o segundo número: "))
#soma = A
#if A >= 0 and B >= 0:
    #    for A in range (A, B+1):
    #       soma += 1
#   for A in range (A,)
#else:
#   print("Operação inválida, tente um número maior que zero")







