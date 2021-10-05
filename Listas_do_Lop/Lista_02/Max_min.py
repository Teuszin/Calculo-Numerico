import math

v = [6.34E0, 9.01E-17, 5.67E-17, 7.04E-5 ,8.44E-4,  3.68E-3, 5.89E0, 9.56e-17, 7.88E-17]

a = math.fsum(v)
b = sum(v)

print("maximo = {0:1.16f}\nminimo = {1:.16f}".format(a, b))
