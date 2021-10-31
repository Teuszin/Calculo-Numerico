import numpy as np
import math

tamanho = int(input())
matriz = np.zeros((tamanho,tamanho))
sominha = 0
dom_linha = 0
dom_col = 0
dominante = 0
teste = 0
igual = 0
seila = []

# Montando a matriz com os valores de inputs:

for i in range (0,tamanho):
    for j in range (0, tamanho):
        matriz[i,j] = float(input())

# verificando dominancia por linha e coluna (o elemento da diagonal principal tem que ser [ em modulo] maior que a soma do restante dos elementos da linha ou coluna):

def dominancia(matriz,tamanho,dom_linha,dom_col,sominha):
    for i in range (0,tamanho):
        for j in range (0, tamanho):
            sominha += abs(matriz[i,j])
        sominha += -abs(matriz[i,i])
        if abs(matriz[i,i]) > sominha:  
            dom_linha += 1
        sominha = 0

    if dom_linha == tamanho:
        return True
    elif dom_linha != tamanho:
        for i in range (0,tamanho):
            for j in range (0, tamanho):
                sominha += abs(matriz[j,i])
            sominha += -abs(matriz[i,i])
            if abs(matriz[i,i]) > sominha:  
                dom_col += 1
        if dom_col == tamanho:
            return True
    else:
        return False

# caso a função retorne True, ela foi dominante por algum dos 2 lados, caso contrário ela irá pro else:

if  dominancia(matriz,tamanho,dom_linha,dom_col,sominha):
    print('a matriz possui dominancia')

# verificando se ela é dominavel trocando as linhas de posição:

else:
    for i in range (0,tamanho):
            for j in range (0, tamanho):
                sominha += abs(matriz[i,j])           
            for x in range (0,tamanho):
                sominha += -abs(matriz[i,x])
                if abs(matriz[i,x]) > sominha:
                    seila.extend([i,x])
                    
                    if i == x:
                        igual += 1
                    if igual >= (tamanho/2):
                        break
                    break

                else:
                    sominha += abs(matriz[i,x])
            sominha = 0

    if igual >= (tamanho/2):
        print('a matriz nao possui dominancia, mesmo se trocar linhas.')
    else:
        print('a matriz possui dominancia se trocar linhas:')
        for y in range(0,int((len(seila))),2):
            print(f'L{seila[y]} vai para L{seila[y+1]}')
