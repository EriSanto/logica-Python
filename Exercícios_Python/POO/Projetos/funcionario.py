class Funcionario:
    def __init__(self, nome, setor,cargo):
        self.nome = nome
        self.setor = cargo
        self.cargo = setor
        
    def apresentar(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa."
    
f1 = Funcionario("Maria", "Coordenadora" , "Vendas" )
f2 = Funcionario("Walter", "Administrador", "Suprimentos")

print(f1.apresentar())
print(f2.apresentar())