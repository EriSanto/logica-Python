# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

nome = input("Nome: ")
nascimento = int(input("Nascimento: "))
ctps = int(input("Carteira de Trabalho (0 não tem): "))

idade = 2026 - nascimento



if ctps != 0:

    ano_contratacao = int(input("Ano de contratação: "))
    salario = int(input("Salário: R$"))

    cadastro = {
        
        'nome':nome,
        'nascimento': nascimento,
        'ctps': ctps,
        'ano_contratacao': ano_contratacao,
        'salario': salario
    }

    cadastro['idade'] = idade

    
    aposentadoria = idade + ((ano_contratacao + 35) - 2026)
    cadastro['aposentado'] = aposentadoria
    
    
    print("======================================================================================================")
    print(cadastro)
    print("Nome:", cadastro['nome'])
    print("Idade:", cadastro['idade'])
    print("CTPS:", cadastro['ctps'])
    print("Contratação:", cadastro['ano_contratacao'])
    print("Salário:", cadastro['salario'])
    print("Aposentado aos:", cadastro['aposentado'])

    
else:
    print("Nome:", nome)
    print("idade:", idade)