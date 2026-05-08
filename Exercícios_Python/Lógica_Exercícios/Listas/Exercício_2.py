nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))

dicionario = {'nome': nome, 'idade': idade, 'Salario':salario}

del dicionario['nome']

print(dicionario)