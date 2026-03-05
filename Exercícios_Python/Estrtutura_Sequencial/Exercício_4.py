#Calculo de média com condição.
nome = input("Digite seu nome:")

a1 = input(f"{nome} irei calcular sua média. Por gentileza, me informe a nota da NP1:")
a2 = input(f"Agora a nota da NP2:")
a3 = input(f"E por último o PIM:")

np1 = float(a1)
np2 = float(a2)
pim = float(a3)

total = (np1 + np2 + pim) / 3

if total >= 7:
 print(f"Aqui está sua média {total}.Você está aprovado")
 
else:
 print(f"Aqui está sua média {total}>. Você está reprovado")
