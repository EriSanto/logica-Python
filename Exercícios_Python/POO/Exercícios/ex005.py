class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def mensagem(self):
        return f'Temos carros da marca {self.marca} do ano {self.ano} da cor {self.cor}'    
        
c1 = Carro('Toyota', 2010, 'Prata')


print(c1.mensagem())


