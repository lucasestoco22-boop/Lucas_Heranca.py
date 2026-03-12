class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return("Olá, meu nome é", self.nome)

    
class Alunos(Pessoa):
    def estudar(self):
        return(self.nome, "esta estudando")
    

class Professor(Pessoa):
    def ensinar(self):
        return(self.nome, "está ensinando")
    