# Faça um programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

nomes = []
idades = []
alturas = []

x = 0

while x < 5:
    
    nome = input("Me informe seu nome: ")
    idade = int(input("Me informe sua idade: "))
    altura = float(input("Me informe sua altura: "))
    
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    
    x +=1
 
print(nomes[::-1])   
print(idades[::-1])
print(alturas[::-1])
