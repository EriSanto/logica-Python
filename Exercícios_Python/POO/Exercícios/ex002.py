class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        
    def inscrever(self, quantidade=1):
        self.inscritos += quantidade
        
class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome,descricao,inscritos)
        self._equipe = []
    
        
canal_lancode = Canal('Lan Code', 'Códigos e gatos', 34000)
canal_guanabara = Canal('Curso em video', 'Paixão por ensinar', 2000000)
canal_duolingo = CanalEmpresarial('Duolingo','ingres', 500000)
print(canal_duolingo.equipe)

