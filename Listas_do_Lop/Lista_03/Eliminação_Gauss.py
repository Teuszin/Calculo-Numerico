import numpy as np

tamanho = int(input())
matriz_coef = np.zeros((tamanho,tamanho))
matriz_cte = np.zeros((tamanho,1))
sominha = 0
teste=np.zeros((len(matriz_coef),1))

matriz_coef_piv=np.copy(matriz_coef)
matriz_cte_piv=np.copy(matriz_cte)
teste_piv=np.copy(teste)

E=0
Ep=0

# Montando a matriz A:

for i in range(0,tamanho):
    matriz_coef[i,i] = 6
    if i+1 < tamanho:
        matriz_coef[i,i+1] = 1
    if i > 0:
        matriz_coef[i,i-1] = 8


# Montando a matriz b:

for j in range (0,tamanho):
        for k in range (0, tamanho):
            sominha += abs(matriz_coef[j,k])
            matriz_cte[j] += sominha
            sominha = 0

for k in range(0,len(matriz_coef)-1):
    for h in range(k+1,len(matriz_coef)): #Escalonamento
        m=-(matriz_coef[h,k]/matriz_coef[k,k])
        matriz_coef[h]=m*matriz_coef[k] +matriz_coef[h]
        matriz_cte[h]=m*matriz_cte[k] +matriz_cte[h] 

for j in range(len(matriz_coef)-1,-1,-1):#Soluções(X)
    R=matriz_cte[j]
    for i in range(0,len(matriz_coef)):
        R=R-(matriz_coef[j,i]*teste[i])
    teste[j]=R/matriz_coef[j,j]

for k in range(0,len(matriz_coef_piv)-1):
    idx=np.argmax(abs(matriz_coef_piv[k:,k]))+k #Pivoteamento Parcial
    matriz_coef_piv[[idx,k]]=matriz_coef_piv[[k,idx]]       
    matriz_cte_piv[[idx,k]]=matriz_cte_piv[[k,idx]]

    for h in range(k+1,len(matriz_coef_piv)): #Escalonamento
        m=-(matriz_coef_piv[h,k]/matriz_coef_piv[k,k])
        matriz_coef_piv[h]= m*matriz_coef_piv[k] +matriz_coef_piv[h]
        matriz_cte_piv[h]= m * matriz_cte_piv[k] + matriz_cte_piv[h]     

for j in range(len(matriz_coef_piv)-1,-1,-1):#Soluções(X)
    R=matriz_cte_piv[j]
    for i in range(0,len(matriz_coef_piv)):
        R=R-(matriz_coef_piv[j,i]*teste_piv[i])
    teste_piv[j]=R/matriz_coef_piv[j,j]

for i in range(tamanho):
    E=E+abs(teste[i])
    Ep=Ep+abs(teste_piv[i])

erro=float(abs(tamanho-E))
erro_com_piv=float(abs(tamanho-Ep))

print("erro_sem_pivo = ", erro, "\nerro_com_pivo = ", erro_com_piv)
