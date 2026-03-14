print("Tela de cadastramento de conta.")
nome = input("Nome:")
senha = input("Senha:")
while len(senha) < 5:
    print("Digite uma senha com mais de 3 digitos!")
    senha = input("Senha:")
 
senha =  int(senha)      
print("<--Cadastrao realizado com sucesso!-->\n")
print(f"Seja bem-vindo, {nome}!")

esco = input("O que deseja fazer?")

if esco == "Fazer lista":
    print("Okay")
    nomelista = input("Nome da Lista:")
    for l in range(1):
        print(f"\n{nomelista}")
             


    
    
    
    
    

