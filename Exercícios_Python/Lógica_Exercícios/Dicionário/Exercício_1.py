

historico_paciente = []

x = 0 

id_contador = 1
while x < 2:
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    sintoma= input("Sintoma: ")
    
    paciente = {
        "ID": id_contador,
        "Nome": nome,
        "Idade": idade,
        "Sintoma": sintoma
    }
  
    
    print(f"Registrado com sucesso paciente {paciente["ID"]} {paciente["Nome"]}!")
    
  

    historico_paciente.append(paciente)
    id_contador += 1
    x += 1
    
    
for p in historico_paciente:
    print(f"Paciente {p['ID']}: {p['Nome']} | Idade: {p['Idade']} | Sintoma: {p['Sintoma']}")
