from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id:str, entrada, tipo:str):
        super().__init__()
        self.id = id
        self.entrada=entrada
        self.tipo=tipo

    def getEntrada(self):
        return self.entrada
    
    def setEntrada(self, entrada):
        self.entrada = entrada
    
    @abstractmethod
    def calcularValor(self,horaSaida):
        pass

    def __str__(self):
        return f"{self.tipo} : {self.id} : {self.entrada}"

class Bike(Veiculo):
    def __init__(self, id: str, entrada):
        super().__init__(id, entrada, "Bike")
         
    def calcularValor(self, horaSaida):
        return 3

class Moto(Veiculo):
    def __init__(self, id: str, entrada):
        super().__init__(id, entrada, "Moto")


    def calcularValor(self, horaSaida):
        calculo = horaSaida - self.entrada
        return calculo/20
    
class Carro(Veiculo):
    def __init__(self, id: str, entrada):
        super().__init__(id, entrada, "Carro")
    
    def calcularValor(self, horaSaida):
        tempo = horaSaida - self.entrada
        valor = tempo / 10
        if valor <5:
            return 5
        return valor

class Estacionamento:
    def __init__(self):
        self.veiculos = []

    def entrar(self, veiculo):
        self.veiculos.append(veiculo)
    
    def sair(self, id, horaSaida, veiculo:Veiculo):
        for c in self.veiculos:
            if c.id != c:
                veiculo.calcularValor
                del(c.id)
            else:
                print("id invalido")
