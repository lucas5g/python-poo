class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id 
        self.titulor = nome 
        self.saldo = saldo 

    def __str__(self):
        return f"A conta {self.id} de {self.titulor} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
            return 

        self.saldo -= valor

c1 = ContaBancaria(112, 'Lucas', 3000)
c1.depositar(500)
c1.sacar(20_000)
print(c1)
