numero_colocado = int(input())

numero_pra_conta = numero_colocado
div = 0
lista_de_primos = []

if (numero_colocado >= 2) and (numero_colocado <= 200):
# \/ Vai ver se o numero atual é primo, caso tenha apenas dois divisoes
 
    while numero_pra_conta != 0:
        for i in range (1, numero_pra_conta + 1):
            if numero_pra_conta % i == 0:
                div += 1 

# \/ caso ele seja primo, vai ser adicionado à lista, incluindo o número colocado

        if div == 2:
            lista_de_primos.append(numero_pra_conta)

# \/ pra que o while se repita, as variaveis vao diminuindo até zerar ( a div tem que resetar pra 0, se não os numeros nunca serão primos)

        numero_pra_conta -= 1
        div = 0

# \/ Aqui, eu fiz isso pra dizer se o número colocado é primo ( é uma das saídas que o programa quer), caso ele seja o primeiro item da lista dos primos, obviamente ele é um, vocês mudar essa parte aqui, da pra fazer de outras formas"

    if numero_colocado == lista_de_primos[0]:
        print(f'{numero_colocado} e primo')  
        
    else:
        print(f'{numero_colocado} nao e primo')
# \/ Aqui, eu tiro o primeiro item da lista, caso ele seja igual o numero que eu coloquei, por que se não ele entra na conta dos "primos abaixo dele"
    if lista_de_primos[0] == numero_colocado:
        del(lista_de_primos[0])

# A outra saida que o programa quer
 
    print(f'existem {len(lista_de_primos)} primos abaixo de {numero_colocado}')
    
# else do if, caso o número não esteja no intervalo entre 2 e 200 que o problema diz

else:
    print("valor de entrada invalido!")