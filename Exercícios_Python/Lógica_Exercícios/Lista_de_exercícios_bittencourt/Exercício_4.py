#Para participar da categoria OURO do 1º. Campeonato Mundial de bolinha de Gude o
#jogador deve pesar entre 70 Kg (inclusive) e 80 kg (inclusive) e medir 1,75 m (inclusive)
#e 1,90 m (inclusive). Leia a altura e o peso de um jogador e determine se o jogador está
#apto a participar do campeonato escrevendo uma das seguintes mensagens, conforme
#cada situação:
#• “RECUSADO POR ALTURA” – somente se a altura do jogador for inválida.
#• “RECUDADO POR PESO”- somente se o peso do jogador for inválido.
#• “TOTALMENTE RECUSADO”- se a altura e o peso do jogador forem inválidos.
#• “ACEITO”- se a altura e o peso do jogador estiverem dentro da faixa
#especificada.




while True:
    alt = int(input("Me informe sua altura: "))
    pes = int(input("Me informe seu peso: "))

    if (alt < 175 or alt > 190) and  (pes < 70 or pes > 80):
        print("Totalmente recusado!")
    else:
        if alt < 175 or alt > 190:
            print("Recusado por altura.")
        elif pes < 70 or pes > 80:
            print("Recusado por peso.")
        else:
            print("Aceito!")
        
    

    