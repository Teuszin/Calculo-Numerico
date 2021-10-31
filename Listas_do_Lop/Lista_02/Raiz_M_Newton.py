import math


def f(A,B,C,D,x):
    return A*math.pow(x,3) + B*math.pow(x,2) + C*x + D

def df(A,B,C,D,x):
    h = 1e-8
    df = (f(A,B,C,D,x+h) - f(A,B,C,D,x)) / h
    return df

A = float(input())
B = float(input())
C = float(input())
D = float(input())
X0 = float(input())
newton = 0
interacoes = 1

while abs(f(A,B,C,D,X0)) > 0.0001:
    newton = X0 - f(A,B,C,D,X0) / df(A,B,C,D,X0)
    X0 = newton
    interacoes += 1
    if interacoes >= 100:
        break

print(round(X0,3),interacoes)
