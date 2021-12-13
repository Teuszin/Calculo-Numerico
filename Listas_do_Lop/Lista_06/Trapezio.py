
num_de_n = int(input())



tabela_x = []
tabela_fx = []

for i in range(num_de_n):
    valor = float(input())
    tabela_x.append(valor)
    
for i in range(num_de_n):
    valor = float(input())
    tabela_fx.append(valor)
    
####################################################

def trapezio(x,fx):
    h = (x[num_de_n - 1] - x[0]) / (num_de_n - 1)
    
    # g(x) da questao:
    funcao = []
    for i in range(0, num_de_n):
        funcao.append (x[i] * fx[i])
        
    # pesos de trapezio ( 2 nos meios e 1's nas pontas):
    pesos = []
    for i in range(0, num_de_n):
        pesos.append(2)
    pesos[0] = 1
    pesos[num_de_n - 1] = 1
    
    # somatório:
    formula= []
    for i in range(0, num_de_n):
        formula.append(funcao[i]*pesos[i])
        
    # integral:
    trapezio = h/2 * sum(formula)
    
    return trapezio

####################################################

def simpson(x,fx):
    h = (x[num_de_n - 1] - x[0]) / (num_de_n - 1)
    
    # g(x) da questao:
    funcao = []
    for i in range(0, num_de_n):
        funcao.append (x[i] * fx[i])
        
    # pesos de simpson ( 2 nos pares, 4 nos impares e 1's nas pontas):
    pesos = []
    for i in range(0, num_de_n):
        if i % 2 == 0:
            pesos.append(2)
        else:
            pesos.append(4)
    pesos[0] = 1
    pesos[num_de_n - 1] = 1
    
    # somatório:
    formula= []
    for i in range(0, num_de_n):
        formula.append(funcao[i]*pesos[i])
        
    # integral:
    simpson = h/3 * sum(formula)
    
    
    return simpson


Trapezio = trapezio(tabela_x,tabela_fx)
Simpson =  simpson(tabela_x,tabela_fx)


print(abs(int((round(Simpson,3))* 1000)-int((round(Trapezio,3))* 1000)))