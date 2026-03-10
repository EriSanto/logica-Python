#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#(codificado da seguinte forma: 1 – álcool; 2 – gasolina), calcule e imprima o valor a ser
#pago pelo cliente, sabendo que o preço da gasolina é de R$ 3,15 e o litro do álcool é de
#R$ 2,83.


alcool_gasolina = input("Olá, me informe se deseja álcool ou gasolina:")
   
if alcool_gasolina == 'Gasolina' or alcool_gasolina == 'gasolina':
    gasolina = float(input("Quantos litros de gasolina você quer?"))
    calculo = gasolina * 3.15
    print(f"Aqui está {gasolina}l: R${calculo:.2f}")
    
elif alcool_gasolina == "Álcool" or alcool_gasolina == 'álcool':
    alcool = float(input("Quantos litro de álcool você quer?"))
    calculo = alcool * 2.83
    print(f"Aqui está {alcool}l: R${calculo:.2f}")
    
else:
    print("Invalido! Informe se deseja álcool ou gasolina.")
    
   
    
    