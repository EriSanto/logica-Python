#Condição para aprovado, reprovado e aprovado por disntinção.
n1 = float(input("Me informe a primeira nota:"))
n2 = float(input("Me informe a segunda nota:"))

media = (n1 + n2)/2

if media == 10:
    print(f"Média {media}. Aprovado com Distinção!")
elif media >= 7:
    print(f"Média {media}.Aprovado!")
else:
    print(f"Média {media}. Reprovado!")