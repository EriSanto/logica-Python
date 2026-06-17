def cadastro():
    
    pacientes = []
    
    

    numero = int(input("Quantos pascientes são: "))
    x = 0
    while x < numero:
        
        nome = input("Nome: ")
        nascimento = int(input("Nascimento: "))
        sintoma = input("Sintoma: ")
        
        idade = 2026 - nascimento
        cadastro = {
            
            'nome':nome,
            'nascimento': nascimento,
            'idade':idade,
            'sintoma':sintoma,
            'id': x
        }
        x += 1
        
        pacientes.append(cadastro)
        
    
    print('=' * 5,"Prontuários",'=' * 5)
    for p in pacientes:
        print()
        
        print(f"Paciente {p['id']} : Nome | {p['nome']}\n             Nascimento | {p['nascimento']}\n             idade | {p['idade']}\n             Sintomas | {p['sintoma']}")
cadastro()


