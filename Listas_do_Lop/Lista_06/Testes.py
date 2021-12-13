 
num_de_n = int(input())

pesos = []
for i in range(0, num_de_n):
    if i % 2 == 0:
        pesos.append(2)
    else:
        pesos.append(4)
pesos[0] = 1
pesos[num_de_n - 1] = 1

print(pesos)