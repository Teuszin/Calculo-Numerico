import math

numero = float(input())

calculo = numero
for i in range(1,410):

    numero = numero / calculo
    
    if numero == 0.0:
        break
    print(numero)
    print(i)
    

print(i)
print(numero)


