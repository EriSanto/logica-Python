from rich import print

class Avatar:
    def __init__(self):
        self.nome = input("Nome: ")
        self.clas = input("Classe: ")
        
    def mensagem(self):
        return f"""O(a) {self.clas}(a) {self.nome} foi conjurado ao mundo de Safar. 
                   Aqui estão seus status."""
        
    def classes(self):
        
        if self.clas == "Mago" or self.clas == "mago":
            return f"""        STATUS 
        
    HP:           :heart: :heart: :heart: :heart:  
    MANA:         :globe_with_meridians::globe_with_meridians::globe_with_meridians::globe_with_meridians:
    Dano:         4
    Armadura:     0
    Carismas:     1
    Destreza:     5
    Inteligência: 4
    
    """
        if self.clas == "Guerreiro" or self.clas == "guerreiro":
            return f"""         STATUS 
        
    HP:           5
    MANA:         0
    Dano:         4
    Armadura:     2
    Carismas:     4
    Destreza:     2
    Inteligência: 4
    
    """
        if self.clas == "Ladrão" or self.clas == "ladrão":
            return f"""         STATUS 
        
    HP:           3
    MANA:         0
    Dano:         1
    Armadura:     0
    Carismas:     6
    Destreza:     5
    Inteligência: 5
    
    """
        if self.clas == "Bardo" or self.clas == "bardo":
            return f"""         STATUS 
        
    HP:           2
    MANA:         5
    Dano:         1
    Armadura:     0
    Carismas:     7
    Destreza:     5
    Inteligência: 5
    
    """
        if self.clas == "Arqueiro" or self.clas == "arqueiro":
            return f"""          STATUS 
        
    HP:           4
    MANA:         0
    Dano:         2
    Armadura:     2
    Carismas:     3
    Destreza:     0
    Inteligência: 3
    
    """

class Ogro:
    def __init__(self,):
        self.vida = 8
        self.dano = 2

class Historia:
    def __init__(self):
        print("Você está andando na floresta e encontra um ogro.")
        self.deci = input("Deseja atacar? [S/N] ")
    
    def decisao(self, orgro_obj):
        self.ogro = orgro_obj
        if self.deci == 'S' or self.deci =='s':
            print(f"Ogro HP: {self.vida} Dano: {self.dano} ")
            
avatar = Avatar()
avatar
print(avatar.mensagem())
print(avatar.classes())
historia = Historia()
print(historia.decisao(8))

                
        
