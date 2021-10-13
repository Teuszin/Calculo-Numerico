import math

def f(x):
    funcao = math.exp(-x**2) - math.cos(x)
    return funcao

a = float(input())
a_salvo = a
b = float(input())
b_salvo = b
L = float(input())

while True:
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(a)*f(b) < 0:
        if abs(f(x)) > L:
            if f(a)*f(x) > 0:
                a = x
            if f(b)*f(x) > 0:
                b = x
            '''
            if f(a) < 0:
                a = x
            if f(b) < 0:
                b = x
            '''
        else: 
            print(x)
            print(abs(f(a_salvo)-f(b_salvo)))
            break
    else:
        print("não há raiz neste intervalo")
        break
