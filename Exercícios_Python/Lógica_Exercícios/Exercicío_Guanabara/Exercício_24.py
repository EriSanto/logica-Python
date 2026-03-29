# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


num = int(input("Digite um número inteiro: "))
num_pick = int(input("Escolha uma das bases  para conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL\nSua opção: "))

if num_pick == 1:
    print(f"Em BINÁRIO: {bin(num)[2:]}")
elif num_pick == 2:
    print(f"Em OCTAL: {oct(num)[2:]}")
else:
    print(f"Em HEXADECIMAL: {hex(num)}")
    