pessoa = []
imc = []

pessoa_quantidade = 2

for i in range(pessoa_quantidade):
    nome = input("Me informe seu nome: ")
    peso = float(input("Me informe seu peso: "))
    altura = float(input("Me informe sua altura: "))

    pessoa.append(nome)

    calculo = peso / (altura * altura)
    
    if calculo <= 16.0:
        imc.append("MAGREZA GRAVE")
        
    elif calculo >= 17.0 and calculo <= 18.5:
        imc.append("MAGREZA LEVE")
        
    elif calculo >= 18.5 and calculo <= 25.0:
        imc.append("SAUDÁVEL")
        
    elif calculo >= 25.0 and calculo <= 30.0:
        imc.append("SOBREPESO")
        
    elif calculo >= 30.0 and calculo <= 35.0:
        imc.append("OBESIDADE GRAU I")
        
    elif calculo >= 35.0 and calculo <= 40.0:
        imc.append("OBESIDADE GRAU II")
        
    elif calculo >= 40.0:
        imc.append("OBEISDADE GRAU III")
 
print(pessoa)   
print(imc)