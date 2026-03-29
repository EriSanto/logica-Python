#   Análise
#len() conta os caracteres
#.count() conta a contidade de letras na frase
#.find() vai achar determinado trecho que voce quiser dentro da frase
#'Suco' in frase vai dizer se existe a palavra Suco na frase  e vai retornar um valor booleano

#  Transformação
#.reaplace('paçoca', 'Banana') ele troca a frase que está na frase por outro que vc escolher
#.upper() e .lower() deixa em maiusculo e minusculo a frase 
#.capitalize() joga todos o caracteres para minusculo e deixa só o primeiro carater da primeira palava
#em maiusculo
#.title() análisa as palavras e troca os caracteres do começo de todas palavras para maiusculo
#.strip() remove todos os espaços do começo e fim da string .rstrip() .lstrip()

#    Divisão
#.split() ele pega onde tem espaço na string e faz uma divisão e cada palavra é colocada dentro de uma lista
#e conta frases tem 
#'-'.join() ele coloca o que fizer dentro dos paranteses entre as palavras dividas com o .split()


# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.




nome = "Eriky Costa Santos"
print(f"Nome normal: {nome}\nNome em maiúsculo: {nome.upper()}\nQuantas letras ao todo (sem considerar os espaços): {len(nome) - nome.count(' ')} \nQuantas letras tem o primeiro nome: {len(nome[0:5])} ")