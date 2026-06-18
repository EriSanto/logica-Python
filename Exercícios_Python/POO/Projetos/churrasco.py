from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self,qunatidade_pessoas):
        self.qtdp = qunatidade_pessoas
        
    def conta(self, consumo=0.400,kg=82.40):
        self.consumo = consumo
        self.kg = kg
        
        panel = Panel.fit( f"""    Análisando o [red]Churrasco[/] de [blue]{self.qtdp} convidados[/]
    Cada participante comerá 0.4Kg e cada Kg custa R$82.40
    Recomendo [blue]comprar {consumo * self.qtdp:.3f}Kg[/] de carne
    O custo total será de [green]R${(consumo * kg) * self.qtdp:,.2f}[/]
    Cada pessoa pagará [green]R${((consumo * kg) * self.qtdp)/ self.qtdp:,.2f}[/] para participar.""")
        
        return panel
        
c1 = Churrasco(2)
print(c1.conta())