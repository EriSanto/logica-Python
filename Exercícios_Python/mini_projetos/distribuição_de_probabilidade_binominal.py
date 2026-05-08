import math

n = int(input("Me informe o valor de N: "))
x = int(input("Me informe o valor de X: "))


coeficiente = math.comb(n,x)

fx = 0.3 ** x

elevado = n-x

fase3 = (1 - 0.3) ** (n-x)

calculo = coeficiente * fx * fase3


print(f"{calculo:.3f}")
