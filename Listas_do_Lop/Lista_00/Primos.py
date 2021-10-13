numero_colocado = int(input())

numero_pra_conta = numero_colocado
div = 0
lista_de_primos = []

if (numero_colocado >= 2) and (numero_colocado <= 200):
    while numero_pra_conta != 0:
        for i in range (1, numero_pra_conta + 1):
            if numero_pra_conta % i == 0:
                div += 1 

        if div == 2:
            lista_de_primos.append(numero_pra_conta)

        numero_pra_conta -= 1
        div = 0
    
    if numero_colocado == lista_de_primos[0]:
        print(f'{numero_colocado} e primo')  
        
    else:
        print(f'{numero_colocado} nao e primo')

    if lista_de_primos[0] == numero_colocado:
        del(lista_de_primos[0])
       
    print(f'existem {len(lista_de_primos)} primos abaixo de {numero_colocado}')
    

else:
    print("valor de entrada invalido!")


