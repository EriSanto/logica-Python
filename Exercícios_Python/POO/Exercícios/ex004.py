class Aluno:
    def __init__(self):
        self.nome = 'Eriky'
        self.turma = '1 Ano-D'
        self.media = 6
    def aprovado_reprovado(self):
        
        if self.media >= 7:
            return f"Turma: {self.turma}\nAluno: {self.nome}\nMédia: {self.media}\nAprovado!"
        else:
            return f"Turma: {self.turma}\nAluno: {self.nome}\nMédia: {self.media}\nReprovado!"

a1 = Aluno()
print(a1.aprovado_reprovado())
            