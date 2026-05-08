numero = 1
numero_tentativas = 0
while numero != 0:
   
     numero = int(input("Ensira um número: "))
     numero_tentativas += 1
     if numero > 0:
         print("Número posivito. Errado!")
         escolha = input("Deseja tentar de novo?\nS ou N? ")
         if escolha == 'N':
             print("Okay. Até logo!")
             print(f"Número de tentativas: {numero_tentativas}")
             break
     elif numero < 0:
         print("Número negativo. Errado!")
         escolha = input("Deseja tentar de novo?\nS ou N? ")
         if escolha == 'N':
             print("Okay. Até logo!")
             print(f"Número de tentativas: {numero_tentativas}")
             break
     else:
         print("Acertou!")
         print(f"Número de tentativas: {numero_tentativas}")
        
