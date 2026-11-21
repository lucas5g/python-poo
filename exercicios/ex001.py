# Declaração de Classe
class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    # def mensagem(self):
    #     return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"
# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
# print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
# print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
# print(g2)
# print(g2.mensagem())

g3 = Gafanhoto()
# print(g3.mensagem())