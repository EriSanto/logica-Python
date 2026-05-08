pessoa = []
imc = []

quant = int(input("Quantos calculos IMC você deseja fazer? "))

for i in range(quant):
    
    pessoa.append(input("Me informe seu nome: "))
    peso = float(input("Me informe seu peso: "))
    altura = float(input("Me informe seu altura: "))

    calculo =   peso/(altura * altura)

    if calculo <= 18:
        imc.append(print("Baixo peso"))   

    elif calculo >= 19 and calculo <= 24:
        imc.append("Peso normal")
        
    elif calculo >= 25 and calculo <= 29:
        imc.append("Excesso de Peso")
        
    elif calculo >= 30 and calculo <= 34:
        imc.append("Obesidade Grau I")
        
    elif calculo >= 35 and calculo <= 39:
        imc.append("Obesidade Grau II")
        
    elif calculo >= 40:
        imc.append("Obesidade Grau III")

print("Pessoas:", pessoa)
print("IMC:", imc)



# vetor = [10, 20, 30, 40, 50]

# print("For: Mais simples e recomendado") 
# for elemento in vetor:
#     print(elemento)

# print("------------------------------------------------")

# for i in range(len(vetor)):
#     print(f"Indice: {i}, Valor: {vetor[i]}")

# print("------------------------------------------------")

# print("While: Util quando você precisa de controle manual") 
# x = 0

# while x < len(vetor):
#     print(vetor[x])
#     x += 1

# print("------------------------------------------------")

# print("do While: Simulado com while  True + break")
# x = 0
# while True:
#     print(vetor[x])
#     x += 1

#     if x >= len(vetor):
#         break



# vetor = []

# for i in range(5):
#     vetor.append(int(input("Me informe um valor: \n")))
#     print(f"indice {i} no valor {vetor[i]}")

''''import numpy as np

valores = []
pessoas = []

quant = int(input("Informe o tamanho da lista: "))

for i in range(quant):
   valores.append(int(input("Entre com valor = ")))
   pessoas.append(str(input("Entre com o nome = ")))

for i in range(len(valores)):
    print(f"indice: {i}, Valor: {valores[i]}")
    print(f"Indice: {i}, Pessoa: {pessoas[i]}")
print(f"Valores: ", valores)
print(f"Pessoas:", pessoas)

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

soma = v1 + v2
mult = v1 * v2

print("V1:", v1)
print("V2:",v2)
print("Soma:",soma)
print("Mult:", mult)'''
