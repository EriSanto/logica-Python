class ContaBancaria:
    def __init__(self, nome, id, saldo = 0):
        self.titular = nome
        self.id = id
        self.saldo = saldo
        
    def __str__(self):
        return f"Conta {self.id} do titular {self.titular} criada com sucesso!"
    
    def depositar(self, valor):
        self.saldo += valor
        
        return f"R${valor} depositado na conta. Situação atual R${self.saldo}."
        
    def sacar(self, valor):
        self.saldo -= valor
        
        if valor > self.saldo:
            return f"Saldo de R${valor} insuficiente na conta."
        else:
            return f"Valor de R${valor} sacado com sucesso. Valor atual R${self.saldo}."


c1  = ContaBancaria("Marcos", 227, 100)
print(c1.depositar(200))
print(c1.sacar(20))
            