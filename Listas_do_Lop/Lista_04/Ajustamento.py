import numpy as np
import math


def g0(x):
    return x**2

def g1(x):  
    return  x 

def g2(x):
    x = 1
    return x

def g3(x):
    return math.cos(x)

def P(a,b,c,d,x):
 
    return (a * (math.pow(x,2))) + (b * x) + c + (d * math.cos(x))

######################################
#            Começa Aqui             #
######################################

componentes_vetor= []    #X
componentes_funcao = []  #F


for i in range (0, 5):
    valor = float(input())
    componentes_vetor.append(valor)

for i in range (0, 5):
    valor = float(input())
    componentes_funcao.append(valor)
    
m_coef_A =[[0., 0., 0., 0.],[0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.]]
m_coef_B = [0., 0., 0., 0.]

for i in range(len(componentes_vetor)):
    m_coef_A[0][0] += g0(componentes_vetor[i]) * g0(componentes_vetor[i])
    m_coef_A[1][1] += g1(componentes_vetor[i]) * g1(componentes_vetor[i])
    m_coef_A[2][2] += g2(componentes_vetor[i]) * g2(componentes_vetor[i])
    m_coef_A[3][3] += g3(componentes_vetor[i]) * g3(componentes_vetor[i])
    
    m_coef_A[0][1] += g0(componentes_vetor[i]) * g1(componentes_vetor[i])
    m_coef_A[0][2] += g0(componentes_vetor[i]) * g2(componentes_vetor[i])
    m_coef_A[0][3] += g0(componentes_vetor[i]) * g3(componentes_vetor[i])
    
    m_coef_A[1][2] += g1(componentes_vetor[i]) * g2(componentes_vetor[i])
    m_coef_A[1][3] += g1(componentes_vetor[i]) * g3(componentes_vetor[i])
    m_coef_A[2][3] += g2(componentes_vetor[i]) * g3(componentes_vetor[i])
    
    m_coef_B[0] += g0(componentes_vetor[i]) * componentes_funcao[i]
    m_coef_B[1] += g1(componentes_vetor[i]) * componentes_funcao[i]
    m_coef_B[2] += g2(componentes_vetor[i]) * componentes_funcao[i]
    m_coef_B[3] += g3(componentes_vetor[i]) * componentes_funcao[i]
    

m_coef_A[1][0] = m_coef_A[0][1]
m_coef_A[2][0] = m_coef_A[0][2]
m_coef_A[3][0] = m_coef_A[0][3]
m_coef_A[2][1] = m_coef_A[1][2]
m_coef_A[3][1] = m_coef_A[1][3]
m_coef_A[3][2] = m_coef_A[2][3]


a, b, c, d = np.linalg.solve(m_coef_A, m_coef_B) 
    

print(round(P(a, b, c, d, 1.1),6), round(P(a, b, c, d, 4.3),6))
