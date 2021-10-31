import numpy as np
import math

tamanho = int(input())
matriz = np.zeros((tamanho,tamanho))
sominha = 0
dom_linha = 0
dom_col = 0
dominante = 0
teste = 0



# Montando a matriz com os valores de imputs:

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


if  dominancia(matriz,tamanho,dom_linha,dom_col,sominha):
    print('É dominante')

else:
    while teste != 1:
        for i in range (0,tamanho):
            for j in range (0, tamanho):
                matriz[[i, j]] = matriz[[j, i]]
                for x in range (0,tamanho):
                    for y in range (0, tamanho):
                        matriz[[x, y]] = matriz[[y, x]]
                        if  dominancia(matriz,tamanho,dom_linha,dom_col,sominha):
                            print('É dominante')
                            teste = 1
                            print(f'{i} trocou por {j} primario')
                            print(f'e {x} trocou por {y} secundario')
                            break
            
            
        