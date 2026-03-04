 #listagem.
'''n1 = [2,5,7,8,4]

total = sum(n1) / len(n1)

print(total)'''

#Listagem de nominal.
'''nome = input("Digite seu nome:")

idade = input("Digite sua idade:")

nascimento = input("Digite sua data de nascimento:")

cidade = input("Onde você mora:")

dados = nome, idade, nascimento, cidade

print(f"Aqui estão seus dados: {dados}") '''


#Calculo de média.
'''a1 = input("Digite numero: ")
a2 = input("Digite numero: ")

n1 = float(a1)
n2 = float(a2)

total =  (n1 + n2) / 2

print(total)'''

#Calculo de média com condição.
'''nome = input("Digite seu nome:")

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
 print(f"Aqui está sua média {total}>. Você está reprovado")'''

#Calculo de salário com descontos.
vh = float(input())
vm = float(input())

sb = vh * vm

ir = sb * (11 / 100)
inss = sb * (8 / 100)
s = sb * (5 / 100)

l1 = sb - ir
l2 = l1 - inss
l3 = l2 - s
print(f"+ Salário Bruto:R${sb}. -IR(11%):R${ir}. -INSS(8%):R${inss}. -Sindicato(5%):R${s}. = Salário Liquido :R${l3}" )