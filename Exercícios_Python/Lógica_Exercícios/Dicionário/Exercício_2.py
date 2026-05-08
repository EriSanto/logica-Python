lista_filmes = []
x = 0

while x < 2:
    nome = input("Nome do filme: ")
    ano = int(input("Ano de lançamento: "))
    genero = input("Genero: ")
    
    

    filme = {'nome':nome, 
            'ano':ano,
            'genero': genero
            }
    
    lista_filmes.append(filme)

    
    
    x += 1


print(lista_filmes[1]['nome'], lista_filmes[0]['ano'])



