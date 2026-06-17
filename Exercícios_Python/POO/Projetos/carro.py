# Crie uma classe Carro com os seguintes atributos: marca, modelo, ano e velocidadeAtual.
# Crie um método chamado acelerar() que aumente a velocidade em \(10\) km/h.Crie um método frear()
# que diminua a velocidade em \(10\) km/h (a velocidade não pode ficar negativa).Crie um método
# exibirDetalhes() que imprima as informações do carro.

class Carro:
    
    def __init__(self, marca, modelo, ano, velocidadeAtual=10):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.vel_atual = velocidadeAtual
        
    def __str__(self):
        return f"Velocidade atual {self.vel_atual}km/h."
    
    def acelerar(self, aumetar):
        self.vel_atual += aumetar
        return f"Acelerei {aumetar}km/h, velocidade atual {self.vel_atual}km/h."
    
    def frear(self, diminuir):
        self.vel_atual -= diminuir
        
        if self.vel_atual <= 0:
            return f"Freei {diminuir}km/h. Carro parou!"
        else:
            return f"Freei {diminuir}km/h, velocidade atual {self.vel_atual}km/h."
       
c1 = Carro("Toyota", "Corolla", 1966, 10)
print(c1)
print(c1.acelerar(50))


