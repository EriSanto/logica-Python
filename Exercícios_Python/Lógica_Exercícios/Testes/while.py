'''num = 1

while (num <= 100):
    print(num)
    num += 1
print('Laço encerrado')'''

'''nome = None

while True:
    print('Digite seu nome, ou X para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}!')
print("Até logo!")'''
    
    
    
'''while True:
    
    num = int(input("Me inform um número de 0 a 10:"))
    if num < 0 and num > 10:
     break 
 '''
 
'''num = 1
 
while num <=10:
    print(num)
    num += 1'''


'''while True:
    
    idade = int(input("Me informe sua idade:")) 
    if idade >= 18:
     print("voce ja tem idade")
    else:
        print("Me informe uma idade valida")
    if idade >=18:
        break
    '''
    
'''while True:
    
    idade = int(input("Me informe sua idade:"))
    altura = float(input("Me informe sua altura"))
    if (idade < 18) and (altura < 1.80):
       print("Me informe uma idade e altura valida.") 
    elif (idade >= 18) and (altura >= 1.80):
     print("Você está liberado para ir.")
     break
    '''
    
'''print("Olá irei fazer seu cadasto no nosso sistema.")

Nome = input("Me informe seu nome:")
peso = float(input("Me informe seu peso:"))
idade = int(input("Me informe sua idade:"))
estado = input("Me informe o estado onde você mora:")

while True:
    if (estado != "SP"):
        print("Esse cadastro apenas para o estado de SP")
        estado += 1
        
    else:
        print("Cadastro feito com sucesso!")
        break     
'''



'''while True:
    numero = int(input("Me informe um número entre zero e dez:"))
    if (numero > 0) and (numero <= 10):
        print("Número válido!")
        break
    else:
        print("Me informe um número válido")'''
        
#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

'''while True:
    
    nome = input("Me informe seu nome:")
    senha = input("Me informe sua senha:")
    
    if senha == nome:
     print("INVALIDA! Informe uma senha que não seja igual ao seu nome!")
    else:
        print("Bem-vindo!")
        break'''
        
        
nome = input("Me informe seu nome:")
while len(nome) < 3:
    print("Me informe um nome com mais de três letras!")
    nome = input("Me informe seu nome:")
idade = int(input("Me informe sua idade:"))
while  not 0 < idade < 150:
    print("Me informe uma idade entre 0 e 150!")
    idade = int(input("Me informe sua idade:"))
salario = float(input("Me informe seu salário:"))
while salario <= 0:
    print("Me informe um salário maior que zero!")
    salario = float(input("Me informe seu salario:"))
    
print(f"---- Informações ----")
print("Nome: ", nome)
print("Idade: ", idade)
print("Salário: ", salario)

    
    
        
        