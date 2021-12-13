import math
import numpy as np

# Interpolação de Gregory-Newton 
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
  
# Valor para interpolar (exemplo):
xp = float(input())

# Número de valores dados
x = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8]
n = len(x)

y=[11.02,13.46,16.44,20.08,24.53,29.96,36.59,44.70]



Ds=np.zeros((n,n))
Ds[0] = y




# Calculando a diferença de Gregory-Newton
# tabela
for i in range(1, n):
    for j in range(0, n - i):
        Ds[i,j] = Ds[i-1,j+1] - Ds[i - 1,j]


# inicializando z e soma

z_cal = np.zeros(n)
z_cal[0] = 1
z=(xp-x[0])/(x[1]-x[0]) 
for i in range(1, n):
    z_cal[i] = z_cal[i-1] * (z+1-i)
    
sum = 0
for i in range(n):
    sum += (Ds[i,0] * z_cal[i])/fact(i)

print(int(10e6 * abs(math.exp(xp)-sum)) - int(100 * abs(Ds[7,0])))