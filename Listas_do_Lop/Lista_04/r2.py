import math
import numpy as np
from math import e

def P0(x):
    return 7816.273180 * (1-math.pow(e, -0.0011752387 * x))

def P1(x):
    return 1.617067 * (math.pow(e,1.153090 * x))

def P2(x):
    return 6.550502 + 18.313747 * np.log(x)

def P3(x):
    return 104.912790 * math.pow(e, -3.483633 / x )

valores_x = [] 
valores_f = []

for i in range (0, 5):
    valor = float(input())
    valores_x.append(valor)

for i in range (0, 5):
    valor = float(input())
    valores_f.append(valor)
    
R2_p0 = 0.; R2_p1 = 0.; R2_p2 = 0.;R2_p3 = 0.
f_med = 0.

aux1_p0 = 0.; aux2_p0 = 0.
aux1_p1 = 0.; aux2_p1 = 0.
aux1_p2 = 0.; aux2_p2 = 0.
aux1_p3 = 0.; aux2_p3 = 0.

# calculo da media
for i in range(len(valores_x)):
  f_med += valores_f[i]
f_med = f_med/5

for i in range(len(valores_x)):
    aux1_p0 += (P0(valores_x[i]) - valores_f[i])**2
    aux1_p1 += (P1(valores_x[i]) - valores_f[i])**2
    aux1_p2 += (P2(valores_x[i]) - valores_f[i])**2
    aux1_p3 += (P3(valores_x[i]) - valores_f[i])**2
    aux2_p0 += (P0(valores_x[i]) - f_med)**2
    aux2_p1 += (P1(valores_x[i]) - f_med)**2
    aux2_p2 += (P2(valores_x[i]) - f_med)**2
    aux2_p3 += (P3(valores_x[i]) - f_med)**2
  
# calculo do coeficiente R²
R2_p0 = 1 - aux1_p0/(aux1_p0 + aux2_p0)
R2_p1 = 1 - aux1_p1/(aux1_p1 + aux2_p1)
R2_p2 = 1 - aux1_p2/(aux1_p2 + aux2_p2)
R2_p3 = 1 - aux1_p3/(aux1_p3 + aux2_p3)

valores_r2 = []
valores_r2.append(R2_p0)
valores_r2.append(R2_p1)
valores_r2.append(R2_p2)
valores_r2.append(R2_p3)

valores_r2.sort(reverse = True)

for i in range (0, 4):
    if valores_r2[i] == R2_p0:
        print(f'P0  R^2 = {valores_r2[i]:.6f}')
    elif valores_r2[i] == R2_p1:
        print(f'P1  R^2 = {round(valores_r2[i],6):.6f}')
    elif valores_r2[i] == R2_p2:
        print(f'P2  R^2 = {round(valores_r2[i],6):.6f}')
    elif valores_r2[i] == R2_p3:
        print(f'P3  R^2 = {round(valores_r2[i],6):.6f}')
        