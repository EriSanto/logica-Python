# Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Me informe seu nome:")
while len(nome) < 3:
    print("Me informe um nome com mais de três caracteres!")
    nome = input("Digite seu nome:")
    
idade = int(input("Me informe sua idade:"))
while idade <= 0 or idade >= 150:
     print("Idade invalida!")
     idade = int(input("Me informe uma idade entre 0 e 150:"))
    
salario = float(input("Me informe seu salário:"))
while salario <= 0:
     print("Me informe uma renda maior que zero!")
     salario = float(input("Me informe seu salário:"))
 
     
estado_civil = input("Me informe seu estado civíl: s,c,v,d ?")
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
  print("Valor não reconhecido! Informe entre: s,c,v,d ")
  estado_civil = input("Estado Civíl:")

print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nEstado Civíl:{estado_civil}")




    