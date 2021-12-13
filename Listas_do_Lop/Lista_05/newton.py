def interpNewton_F3(x, y, xi):
  #Número de dados
  n = len(x)
  #Inicialização da diferença dividida: n x n
  fdd = [[None for x in range(n)] for x in range(n)]
  #Valores da função f(X) em vários pontos
  yint = [None for x in range(n)]
    
  #Encontrando diferenças divididas.
  for i in range(n):
    fdd[i][0] = y[i]
  for j in range(1,n):
    for i in range(n-j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])
    
  # Imprimindo diferenças divididas.

    
  #Interpolação para xi.
  xterm = 1
  yint = fdd[0][0]
  for order in range(1, n):
    xterm = xterm * (xi - x[order-1])
    yint = yint + fdd[0][order]*xterm
    
  #Retornando g(xi).
  return yint ,fdd[0][3]

valores_x = []
valores_y = []

for i in range (0, 4):
    valor = float(input())
    valores_x.append(valor)

for i in range (0, 4):
    valor = float(input())
    valores_y.append(valor)

xp = 100

yp, F3 = interpNewton_F3(valores_x, valores_y, xp)


# Valor pro F3;

print(int(abs(round(10000*(F3),2))))
# Valor pro Yp:

print(int(round(yp,2)))
