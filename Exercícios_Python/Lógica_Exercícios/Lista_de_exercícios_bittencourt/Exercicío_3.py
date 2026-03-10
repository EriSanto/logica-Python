#Faça um algoritmo que leia a idade de um atleta e escreva em que categoria ele se
#enquadra, seguindo o quadro abaixo:

idade = int(input("Me informe sua idade:"))

if idade >= 5 and idade <= 10:
    print("Categoria Infantil.")
elif idade >= 11 and idade <= 17:
    print("Categoria Juvenil.")
elif idade >= 18 and idade <= 30:
    print("Categoria Profissional.")
elif idade >= 30:
    print("Categoria Sênior.")
else:
    print("Competidores abaixo dos 5 anos de idade não são permitidos.")
    
