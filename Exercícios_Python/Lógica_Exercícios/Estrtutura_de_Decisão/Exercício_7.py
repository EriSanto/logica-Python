#Faça um programa que leia três números e mostre-os em ordem decrescente:
numero_1 = int(input("Me informe um número: "))
numero_2 = int(input("Me informe um segundo número: "))
numero_3 = int(input("Me informe mais um terceiro número: "))


if numero_1 < numero_2 < numero_3:
    print(f"A ordem decrescente dos números: {numero_3} - {numero_2} - {numero_1}")
elif numero_1 > numero_2 > numero_3:
    print(f"A ordem decrescente dos números: {numero_1} - {numero_2} - {numero_3}")
elif numero_1 < numero_2 > numero_3:
    print(f"A ordem decrescente dos números: {numero_2} - {numero_3} - {numero_1}")
elif numero_1 > numero_2 < numero_3:
    print(f"A ordem decrescente dos números: {numero_1} - {numero_3} - {numero_2}")


