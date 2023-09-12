class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

class Conta:
    def __init__(self):
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"Depósito: +{valor}")

    def sacar(self, valor):
        if valor > 0 and self.saldo - valor >= -self.cliente.renda_mensal:
            self.saldo -= valor
            self.operacoes.append(f"Saque: -{valor}")

class ContaMulher(Conta):
    def __init__(self, cliente):
        super().__init__()
        self.cliente = cliente
        self.cheque_especial = cliente.renda_mensal

    def sacar(self, valor):
        if valor > 0 and self.saldo - valor >= -self.cheque_especial:
            self.saldo -= valor
            self.operacoes.append(f"Saque: -{valor}")

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta_mulher(self, cliente):
        conta = ContaMulher(cliente)
        self.contas.append(conta)
        return conta

    def criar_conta_homem(self):
        conta = Conta()
        self.contas.append(conta)
        return conta