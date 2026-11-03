# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto
    """
    def __init__(self, nome, idade): # Método Construtor
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __str__(self):
        return "Vou te mostrar uma coisa..."

# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2.mensagem())

print(g1.__doc__)