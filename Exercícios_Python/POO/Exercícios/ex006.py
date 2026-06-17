class Aluno:
    def __init__(self,nome,turma,media):
        self.nome = nome
        self.turma = turma
        self.media = media
    
    def mensagem(self):
        return f"Aluno {self.nome} da turma {self.turma} teve a média {self.media}"
    
al = Aluno('Ailson', '3 Ano D', 10)

    
print(al.mensagem())