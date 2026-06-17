class Canal:
    def __init__(self, nome, descricao, inscricao):
        self.nome = nome
        self.descricao = descricao
        self.inscricao = inscricao
        
canal_lancode = Canal('Lan Code', 'Códigos e gatos', 34000)
canal_guanabara = Canal('Curso em video', 'Paixão por ensinar', 2000000)

print(canal_lancode.inscricao)
print(canal_guanabara.descricao)