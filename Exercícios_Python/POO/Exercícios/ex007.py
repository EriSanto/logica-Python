class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
    
    def aniversario(self, contagem=1):
        self.idade += contagem
        
    def mensagem(self):
        return f"O(a){self.nome} e tem {self.idade}."

p1 = Pessoa()
p1.nome = 'Marcia'
p1.idade = 24
p1.aniversario()
print(p1.mensagem())

p2 = Pessoa()
p2.nome = 'Marcos'
p2.idade = 32
p2.aniversario()
print(p2.mensagem())

p1 = Pessoa()
p1.nome = 'Bruna'
p1.idade = 20
print(p1.mensagem())
        