# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.



alunos = []
media = []

alunos_media = [alunos, media]

quantidade_alunos = int(input("Me informe a quantidade de alunos que deseja tirar a média: "))

for a in range(quantidade_alunos):
    aluno = input("Nome do aluno: ")
    n1  = float(input("Nota 1: "))
    n2  = float(input("Nota 2: "))
    n3  = float(input("Nota 3: "))
    n4  = float(input("Nota 4: "))
    
    alunos.append(aluno)
    
    calculo_media = (n1 + n2 + n3 + n4) / 4
    
    media.append(calculo_media)
    
for alu, med in zip(alunos, media):
    if med >= 7.0:
    
     print("Alunos na média:\n")
     print(f"Aluno: {alu}")
     print(f"Media: {med}\n")

    

    
    


