import math

cima = int(input())
baixo = int(input())
direita = int(input())
esquerda = int(input())

cateto_1 = abs(cima - baixo)
cateto_2 = abs(direita - esquerda)

distancia = math.sqrt(math.pow(cateto_1,2) + math.pow(cateto_2,2))

print(int(round(distancia)))