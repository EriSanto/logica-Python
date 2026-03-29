#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


import random
primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")

lista = [primeiro_aluno,segundo_aluno,terceiro_aluno,quarto_aluno]

escolhido = random.choice(lista)


print(f"O aluno escolhido foi, {escolhido}")
