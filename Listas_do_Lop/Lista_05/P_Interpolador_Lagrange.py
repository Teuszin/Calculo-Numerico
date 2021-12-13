import numpy as np


def interpLagrange(xp,x,y,n): 
  # Valor inicial de g(xp).
  yp = 0
  # Interpolação de Lagrange
  for k in range(0,n+1):  
    p = 1
    for j in range(0,n+1):
      if k != j:
        p = p*(xp - x[j])/(x[k] - x[j])
    
    yp = yp + p * y[k]  

  return yp 



# Dados do problema.
x = [0,1,10,15,20,32,59,62,125]
y = [0,4.6,56.4,97.2,136.2,226.2,403.9,440.4,1265.2]

# Ponto da interpolação
#xp = float(input('Entre com xp: ')) #caso queiram inserir manualmente o valor de xp
xp = 1
# Grau da interpolação.
n = 1
# Interpolação de Lagrange.
yp = interpLagrange(xp,x,y,n)

# Valor interpolado encontrado
print('g(%.3f) = %.3f' % (xp, yp))