import math

x = float(input())
n = int(input())
soma = 0
cont = 0
cosseno = math.cos(x)

while cont != n+1:
    soma = soma + ((math.pow(-1,cont) * math.pow(x,(2*cont))) / (math.factorial(2*cont)))
    cont += 1

print(abs(cosseno - soma))