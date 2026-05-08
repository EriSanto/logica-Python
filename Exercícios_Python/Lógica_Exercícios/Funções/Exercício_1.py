# def somar(n1, n2):
#     soma = n1+n2
#     print(soma)
    
# somar(2,2)

# nome = input("Me informe seu nome: ")
# idade = int(input("Me informe sua idade: "))
# sexo = input("Me informe seu sexo: ")


# def pessoa(nome, idade,sexo):
   
#    print(f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}")
# pessoa(nome, idade,sexo)  




# def dinheiro(nome,salario):
#     inss = salario * 0.10
#     vt = salario * 0.06
    
#     calculo = (salario - inss) - vt
    
#     print(nome,"R$",calculo)  
# dinheiro("Fernando",1600)
# dinheiro("Ana",1000)


# nome = input("Nome:")
# salario = float(input("Salaário:"))

# def dinheiro(nome,salario):
#     inss = salario * 0.10
#     vt = salario * 0.06
    
#     calculo = (salario - inss) - vt
    
#     print(nome,"R$",calculo)  
# dinheiro(nome,salario)


# item1 = input("Nome:")
# item2 = input("Nome:")
# item3 = input("Nome:")


# def sacola(item1, item2, item3):
#     itens = [item1, item2, item3]

#     for i in itens:
#         if i == "Danone":
#             continue
#         print(i)
# sacola(item1, item2, item3)



def objeto():
    pessoa = []

    x = 0
    while True:
        
        atributo = input("Digite um atributo: ")
        
        add_atributo = pessoa.append(atributo)
        x += 1
        print(pessoa)
        
        continuar = input("Deseja continuar, s ou n?  ")
        
        if continuar == 'n':
            print(pessoa)
            break
        
objeto()
