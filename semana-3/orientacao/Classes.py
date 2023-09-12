class Carro:
    def _init_(self, ligado, cor, modelo, velocidade):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
    
    def Ligar(self):
        print('Ligando')

    def Desligar(self):
        print('Desligando')

    def Acelerar(self):
        print('Acelerando')

    def Desacelerar(self):
        print('Desacelerando')

    def Carro_status(self):
        print(self.ligado, self.cor, self.modelo, self.velocidade)

carro1 = Carro('Desligado', 'Rosa', 'Verona', '0km')
carro1.Carro_status()
carro1.Acelerar()