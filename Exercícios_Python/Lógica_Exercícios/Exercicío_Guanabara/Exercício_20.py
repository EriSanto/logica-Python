#  O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

escolhido = random.sample(lista,4)

print(f"Os vencedores na ordem são: {escolhido}")

