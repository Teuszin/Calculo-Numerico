lado = float(input())
altura = float(input())
numero = int(input())
area_1 = lado * altura
area_2 = 0

erro_max = 0

# Fazer o somatorio porposto pelo exercicio

for x in range(-50,51):
    atual = numero + x
    for j in range (0,atual):
        area_2 += lado * (altura/(atual))
    modulo_dif = abs(area_1 - area_2)

# Pegar o maior erro maximo
    if erro_max < modulo_dif:
        erro_max = modulo_dif
        num = atual
        
# resetar o somatorio
    
    area_2 = 0
        

print("n_max = {0:d}\nerro_maximo = {1:.14f}".format(num,erro_max))



