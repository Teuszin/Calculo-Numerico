import math

numero = (int(input()))
intervalo = int(input())
i = 0
j = 0
lista_divisores =[]
lista_dos_perfeitos = []
if (numero >= 2) and (intervalo <= 1000):
    for i in  range(numero, intervalo + 1): 
        
        for j in range (1,i+1):

            if (i % j) == 0:
                lista_divisores.append(i // j)

        del(lista_divisores[0])
        
        soma_dos_divisores = (math.fsum(lista_divisores))
        if soma_dos_divisores == i:
            lista_dos_perfeitos.append(i)
            
        lista_divisores.clear()

    if len(lista_dos_perfeitos) == 0:
        print('nao ha numeros perfeitos no intervalo escolhido!')
    else:
        print(f'{lista_dos_perfeitos}')
else:
    print("valor de entrada invalido!")