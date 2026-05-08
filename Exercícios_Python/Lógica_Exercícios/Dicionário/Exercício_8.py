# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
# o total de gols feitos durante o campeonato.

# nome = input("Nome jogador: ")

# gols = []
# x = 0

# for i in range(1,6):
#     jogo = int(input(f"\nJogo {i}\nNúmero de gols: "))
#     gols.append(jogo)
    
# total_gols = sum(gols)
    
# jogador = {
    
#     'nome': nome,
#     'gols': gols,
#     'total': total_gols
    
# }

# print(jogador)

# print(f"O jogador {nome} jogou 5 partidas.")
# print(f"Na partida 1, fez {jogador['gols'][0]}")
# print(f"Na partida 2, fez {jogador['gols'][1]}")
# print(f"Na partida 3, fez {jogador['gols'][2]}")
# print(f"Na partida 4, fez {jogador['gols'][3]}")
# print(f"Na partida 5, fez {jogador['gols'][4]}")
# print(f"Total de {jogador['total']} gols.")


nome = input("Nome jogador: ")

qtd_jogos = int(input("Quantas partidas foram jogadas? "))

qtd_jogos += 1

gols = []
x = 0

for i in range(1,qtd_jogos):
    jogo = int(input(f"\nJogo {i}\nNúmero de gols: "))
    gols.append(jogo)
    
total_gols = sum(gols)
    
jogador = {
    
    'nome': nome,
    'gols': gols,
    'total': total_gols
    
}

print("=========================================================\n")
print(f"O jogador {nome} jogou {qtd_jogos} partidas.\n")

for j, g in enumerate(gols, start=1):
        
    print(f"Na partida {j}, fez {g} gols.")
print(f"Total de gols: {total_gols}")
   