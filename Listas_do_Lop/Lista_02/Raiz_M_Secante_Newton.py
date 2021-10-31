import math


def f(A,B,C,D,x):
    return A*math.pow(x,3) + B*math.pow(x,2) + C*x + D

def df(A,B,C,x):
    h = 1e-8
    return 3*A*math.pow(x,2) + 2*B*x + C
    

A = float(input())
B = float(input())
C = float(input())
D = float(input())
U = float(input())
V = float(input())
X0 = (U + V) / 2
x_ant = X0
newton = 0
secante = 0
interacoes = 1

newton = X0 - f(A,B,C,D,X0) / df(A,B,C,X0)

while abs(newton - X0) > 1e-4:
    if abs(df(A,B,C,newton)) <= 1e-3:
        break
    else:
        X0 = newton
        newton = X0 - f(A,B,C,D,X0) / df(A,B,C,X0)
        interacoes += 1
        


if abs(df(A,B,C,newton)) < 1e-3:
    
    secante = (V * f(A,B,C,D,U) - U * f(A,B,C,D,V)) / (f(A,B,C,D,U) - f(A,B,C,D,V))
    while abs(secante-V) > 1e-4:
        U = V
        V = secante
        secante = (V * f(A,B,C,D,U) - U * f(A,B,C,D,V)) / (f(A,B,C,D,U) - f(A,B,C,D,V))
        
        
    print(round(secante,3),interacoes)
else:
    print(round(newton,3),0)