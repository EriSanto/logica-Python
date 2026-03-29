# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nasci = int(input("Ano de nascimento: "))


idade = 2026 - nasci
alistamento = 2026 - idade

if idade < 18:
    print(f"Quem nasceu em {nasci} tem {idade} em 2026")
    print(f"")

print(idade)