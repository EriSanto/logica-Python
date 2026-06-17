# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


pessoas = []

x = 0
soma = 0

while True:
    
    nome = input("Nome: ")
    sexo = input("Sexo: (M/F)? ")
    idade = int(input("Idade: "))
    
  
    pessoa = {
            
            'nome':nome,
            'sexo':sexo,
            'idade':idade
        }
    
    x += 1

    pessoas.append(pessoa)
    
    

    continu = input("Deseja continuar: (S/N)? ")
    
    if continu == 'n':
        
       
        print("\n==================================================================\n")
        print(f"A) Pessoas cadastradas foram {x}")

        for p in pessoas:
            soma += p['idade']
            
            media = soma / x
        print(f"B) A média de idade é de {media:.2f}")
        
    
        print("C) Mulheres cadastradas: ",)
                    
        for p in pessoas:
            if p['sexo'] == 'F' or p['sexo'] == 'f':
                print(f"  => {p["nome"]};")
                
        print(f"D) Pessoas com idade acima de média:")
        for i in pessoas:
            if i['idade'] >= media:
                print(f"  => {i["nome"]};")
        break

            
            
        




    
    

