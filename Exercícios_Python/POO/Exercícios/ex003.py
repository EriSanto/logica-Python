class Alunos:
    def __init__(self):
        self.nome =  ''
        self.media = 0
        self.turma = ''
    def aprovado_reprovado(self):
        
        if self.media >= 7:
            return f"Turma: {self.turma} Aluno: {self.nome} tirou nota {self.media}. Aprovado!"
        else:
            return f"Turma: {self.turma} Aluno: {self.nome} tirou nota {self.media}. Reprovado!"
        
al1 = Alunos()
al1.turma = input("Turma: ")
al1.nome = input("Nome do aluno: ")
al1.media = int(input("Média: "))

print(al1.aprovado_reprovado())

            
        
        
