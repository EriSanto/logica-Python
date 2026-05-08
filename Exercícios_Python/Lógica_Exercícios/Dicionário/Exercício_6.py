# Faça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.



nome = input("Nome aluno: ")
media = float(input("Média: "))

aluno_dados = {
    'nome':nome, 
    'media': media
    }

if media >= 7.0:
    
    aluno_dados['situacao'] = "Aprovado"
    
    print(aluno_dados)
    print()
    
    print(f"Aluno {aluno_dados['nome']}")
    print(f"Média {aluno_dados['media']}")
    print(f"Situação {aluno_dados['situacao']}")

else:

    aluno_dados['situacao'] = "Reprovado"
    
    print(aluno_dados)
    print()
    
    print(f"Aluno {aluno_dados['nome']}")
    print(f"Média {aluno_dados['media']}")
    print(f"Situação {aluno_dados['situacao']}")
    