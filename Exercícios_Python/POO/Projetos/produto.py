from rich import print
from rich.panel import Panel
from rich.text import Text

# panel = Panel("Exemplo\nfoda", width=10, )

# print(panel)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        texto = Text(f"{self.nome}\n---------------\n....R${self.preco:,.2f}....", justify="center")
        return Panel.fit(texto, title="Produto"  )
    
p1 = Produto("Playstation 5",3000)
p2 = Produto("Nintendo Switch 2",2000)

print(p1.etiqueta())
print(p2.etiqueta())