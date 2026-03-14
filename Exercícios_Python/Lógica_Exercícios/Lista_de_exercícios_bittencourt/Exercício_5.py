#A Federação de Futebol contratou você para escrever um programa para fazer uma
#estatística de vários jogos (Flamengo e Vasco). Escreva um algoritmo para ler o número
#de gols marcados pelo Flamengo e o número de gols marcados pelo Vasco em um jogo,
#imprimindo o nome do vencedor ou a palavra EMPATE. Logo após imprima a mensagem
#“Novo jogo (1 – Sim; 2 – Não)?”. Se a resposta for 1 o algoritmo deve ser executado
#novamente solicitando o número de gols marcados em uma nova partida, caso contrário
#deve ser encerrado e impresso:
#a. Quantos jogos fizeram parte da estatística.
#b. O número de vitórias do Flamengo.
#c. O número de vitórias do Vasco.
#d. O número de empates.
#e. Uma mensagem indicando qual time venceu o maior número de jogos ou NÃO
#HOUVE VENCEDOR.


numero_de_jogos = 0
vitoria_flamengo = 0
vitoria_vasco = 0
empate = 0
    
while True: 
    
  gols_flamengo = int(input("Me informe o número de gols do Flamengo:")) 
  gols_vasco = int(input("Me informe o número de gols do Vasco:"))
  
  numero_de_jogos  += 1
  
  if gols_flamengo > gols_vasco:
    vitoria_flamengo += 1
    print("FLAMENGO VENCEDOR!")
  elif gols_vasco > gols_flamengo:
    vitoria_vasco += 1
    print("VASCO VENCEDOR!")
  elif gols_flamengo == gols_vasco:
    empate += 1
    print("EMPATE!")
    
  novo_jogo = input("Novo Jogo?\n1 - Sim.\n2 - Não. ") 
  if novo_jogo == 'Não' or novo_jogo == 'não' or novo_jogo == '2':
       
      if vitoria_flamengo < vitoria_vasco:
       print(f"Número de jogo: {numero_de_jogos} ")
       print(f"Número de vitórias do Flamengo: {vitoria_flamengo}")
       print(f"Número de vitórias do Vasco: {vitoria_vasco}")
       print(f"Número de empates: {empate}")
       print(f"Maior taxa de vitórias: Vasco!")
      elif vitoria_flamengo > vitoria_vasco:
        print(f"Número de jogo: {numero_de_jogos} ")
        print(f"Número de vitórias do Flamengo: {vitoria_flamengo}")
        print(f"Número de vitórias do Vasco: {vitoria_vasco}")
        print(f"Número de empates: {empate}")
        print(f"Maior taxa de vitórias: Flamengo!")
      else:
        print(f"Número de jogo: {numero_de_jogos} ")
        print(f"Número de vitórias do Flamengo: {vitoria_flamengo}")
        print(f"Número de vitórias do Vasco: {vitoria_vasco}")
        print(f"Número de empates: {empate}")
        print(f"Maior taxa de vitórias: Não houve vencedor...")
      break 
  
          
          

  


    

    
    

