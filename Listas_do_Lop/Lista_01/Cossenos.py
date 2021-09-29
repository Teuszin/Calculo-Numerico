import math
x = float(input())
n = int(input())
somatorio = 0
i = 0
for i in range(0,n+1):
    somatorio += (math.pow(-1,i) * math.pow(x,(2*i))) / (math.factorial(2*i))

cosseno = math.cos(x)

print(abs(cosseno - somatorio))