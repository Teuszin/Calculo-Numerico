import math
from typing import AsyncContextManager

numero = float(input())
num_salvo = numero
i = 1
j = 1

# \/ Multiplicar o numero por ele mesmo ate o python pifar e ver quantas vezes a operação ocorre
while True:
    numero = numero * num_salvo
    
    if numero == math.inf:
        
        break
    i += 1

# \/ Resetar o numero
numero = num_salvo

# \/ Dividir o numero por ele mesmo ate o python pifar e ver quantas vezes a operação ocorre

while True:
    numero = numero / num_salvo
    if numero == 0.0:
        
        break
    j += 1

# \/ Imprimir
print("n = ",i, "\tinf", "\nm = ",j, "\t0.0")
