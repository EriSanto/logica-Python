class Pessoa:
    """
    Essa classe cria uma pessoa que tem nome e idade.
    
    Para criar uma nova pessoa,use
    variavel = Pessoa(nome, idade)
    """
    def __init__(self, n = "vazio", i = 0):
        self.nome = n
        self.idade = i
    
    def aniversario(self, contagem=1):
        self.idade += contagem
        
    def mensagem(self):
        return f"O(a){self.nome} e tem {self.idade} de idade."
    
    def __str__(self): # Dunder Method. Ao invez de aparecer o endereço da clase, ele chama a mensagem que você desejar colocar. 
            return f"O(a){self.nome} e tem {self.idade} de idade."

p1 = Pessoa('Maria', 17)
p1.aniversario()
print(p1)

#print(p1.__doc__)

        