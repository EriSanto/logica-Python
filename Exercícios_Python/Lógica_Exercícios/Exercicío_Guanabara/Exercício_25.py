#  Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print(f"O PRIMEIRO valor é maior.")
elif num2 > num1:
    print(f"O SEGUNDO valor é maior.")
else:
    print("TODOS OS VALORES SÂO IGUAIS.")
