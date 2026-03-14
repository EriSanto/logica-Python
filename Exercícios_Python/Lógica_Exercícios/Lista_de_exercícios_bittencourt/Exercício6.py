# Escreva um programa para ler um valor A e um valor N. Imprimir a soma do N números
# a partir de A (inclusive). Caso N seja negativo ou zero, deverá ser lido um novo número
# para N (só para N).
# Valores para testes:

a = int(input("Me informe A:")) 
n = int(input("Me informe N:"))
while n <= 0:
   n = int(input("Valores negativos ou zero não são aceitos. Ensira um novo valor de N:"))
n += 1
total = sum(range(a,n))
print(*range(a, n), f'= {total}' )



    

