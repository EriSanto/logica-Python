from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
    
    def add_favoritos(self, game):
        self.favoritos.append((game))
        self.favoritos = sorted(self.favoritos, key=str.lower)

    
    def ficha(self):
        conteudo = f"Nome real: {self.nome}"
        conteudo += f"\nJogos favoritos:"
        for game in enumerate(self.favoritos):
            conteudo += f"{game}"
        painel = Panel.fit(conteudo, title=f"Jogador {self.nick}")
        print(painel)
        
j1 = Gamer("Eriky", "YCarly")
j1.add_favoritos("Mario")
j1.add_favoritos("Zelda")
j1.ficha()
