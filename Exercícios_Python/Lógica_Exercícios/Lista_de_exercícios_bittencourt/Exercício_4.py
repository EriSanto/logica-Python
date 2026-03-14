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

print("Cadastro do Campeonato Mundial de bolinha de Gude")

peso = float(input("Me informe seu peso:"))
altura = float(input("Me informe sua altura:"))

if peso < 70 or peso > 80:
    print("RECUSADO POR PESO!")
elif altura < 1.75 or altura > 1.90:
    print("RECUSADO POR ALTURA!")
else:
    print("ACEITO!")
