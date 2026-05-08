# while True:
#     alt = int(input("Me informe sua altura: "))
#     pes = int(input("Me informe seu peso: "))

#     if (alt < 170 or alt > 190) and  (pes < 70 or pes > 80):
#         print("Totalmente recusado!")
#     else:
#         if alt < 170 or alt > 190:
#             print("Recusado por altura.")
#         elif pes < 70 or pes > 80:
#             print("Recusado por peso.")
#         else:
#             print("Aceito!")


# cont = 1

# while cont <= 3 :

#     compra = float(input("Me informe o valor da compra: "))

#     des_10 = compra * (10 / 100)
#     des_15 = compra * (15 / 100)

#     if compra >= 100.01:
#         print(f"Valor da compra: R${compra}")
#         print(f"Desconto: R${des_10}")
#         print("Valor Total: R$",compra - des_10)
#     elif compra >= 500:
#         print(f"Valor da compra: R${compra}")
#         print(f"Desconto: R${des_15}")
#         print("Valor Total: R$",compra - des_15)
#     else:
#         print(f"Valor da compra: R${compra}")
#         print(f"Desconto: R$0")
#         print("Valor Total: R$",compra)
#     cont +=1

# cont = 0

# while cont < 100:
#     print(cont)
#     cont +=2

import random

# print("---------Escolha 3 frutas-------------")
# frut1 = input("Fruta 1: ")
# frut2 = input("Fruta 2: ")
# frut3 = input("Fruta 3: ")

# sacola = [frut1, frut2, frut3]


# esco_aleato = random.choice(sacola)

# print(esco_aleato)


# sacola = ["Maçã","Uva","Banana","Pera","Melão","Laranja","Maracuja","Melancia","Goiaba","Pitanga"]

# esoco_ale = random.sample(sacola, 3)

# #print(esoco_ale)

# for tirar in sacola:
#     if tirar == "Uva":
#         continue
#     print(tirar)


# for i in range(1,4):
#     print("Tabela",i)
#     for al in range(5):
#         ale = random.randint(1,4)
#         print(ale)




