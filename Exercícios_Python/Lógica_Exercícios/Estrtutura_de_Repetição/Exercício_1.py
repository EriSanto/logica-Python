# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.

nota = int(input("Me informe uma nota entre zero e dez:"))

while nota < 0 or nota >10:
    print("Ensira um valor válido!")
    nota = int(input("Nota:"))
