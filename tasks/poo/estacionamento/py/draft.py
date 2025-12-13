from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id:str, entrada, tipo:str):
        super().__init__()
        self.id = id
        self.entrada:None=entrada
        self.tipo=tipo

    def getEntrada(self):
        return self.entrada
    
    def setEntrada(self, entrada):
        self.entrada = entrada
    
    @abstractmethod
    def calcularValor(self,horaSaida):
        pass

    def __str__(self):
        print(f"{self.tipo} : {self.id} : {self.entrada}")

    


    
        
        
        