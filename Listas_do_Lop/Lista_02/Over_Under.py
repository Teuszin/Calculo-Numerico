import math

numero = float(input())
num_salvo = numero
i = 1
j = 1

while True:
    numero = numero * num_salvo
    
    if numero == math.inf:
        break
    i += 1

numero = num_salvo

while True:
    numero = numero / num_salvo
    if numero == 0.0:
        break
    j += 1

print("n = ",i, "\tinf", "\nm = ",j, "\t0.0")
