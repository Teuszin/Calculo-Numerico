lado = float(input())
altura = float(input())
numero = int(input())
area_1 = lado * altura
area_2 = 0

valor_max = 0

for x in range(-50,51):
    atual = numero + x
    for j in range (0,atual):
        area_2 += lado * (altura/(atual))
    modulo_dif = abs(area_1 - area_2)
    if valor_max < modulo_dif:
        valor_max = modulo_dif
        num = atual
    j = 0
    area_2 = 0
        

print("n_max = {0:d}\nerro_maximo = {1:.14f}".format(num,valor_max))



