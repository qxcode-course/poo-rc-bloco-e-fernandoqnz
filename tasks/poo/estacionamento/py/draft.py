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
    def __init__(self, id: str):
        super().__init__(id,0 , "Bike")
         
    def calcularValor(self, horaSaida):
        return 3

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 0, "Moto")


    def calcularValor(self, horaSaida):
        return (horaSaida - self.entrada) /20
    
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 0, "Carro")
    
    def calcularValor(self, horaSaida):
        valor = (horaSaida - self.entrada)/10
        return max(valor, 5)
class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaAtual = 0 

    def entrar(self, veiculo):
        veiculo.setEntrada(self.horaAtual)
        self.veiculos.append(veiculo)

    
    def sair(self, id):
        achou = False
        for c in self.veiculos:
            if c.id == id:
                valor = c.calcularValor(self.horaAtual)
                print(f"{c.tipo} chegou {c.entrada} saiu {self.horaAtual}. Pagar R$ {valor:.2f}")
                self.veiculos.remove(c)
                achou = True
                return
        if not achou:
            print("id invalido")

    def passarTempo(self,tempo):
        self.horaAtual += tempo

    def __str__(self):
        if not self.veiculos:
            return f"Hora atual: {self.horaAtual}"
        
        linhas = []
    
        underscores_tipo = {
        "Bike": 6,
        "Moto": 6,
        "Carro": 5
        }

        underscores_id = {
        "Bike": 5,
        "Moto": 3,
        "Carro": 3
        }

        for c in self.veiculos:
            tipo_format = "_" * underscores_tipo[c.tipo] + c.tipo
            id_format = "_" * underscores_id[c.tipo] + c.id
            linhas.append(f"{tipo_format} : {id_format} : {c.entrada}")

        linhas.append(f"Hora atual: {self.horaAtual}")
        return "\n".join(linhas)


def main():
    estacionamento = Estacionamento()

    while True:
        line=input()
        args=line.split(" ")
        print(f"${' '.join(args)}")
        cmd = args[0]

        if cmd == "end":
            break
        elif cmd =="show":
            print(estacionamento)
        elif cmd == "tempo":
            estacionamento.passarTempo(int(args[1]))
        elif cmd == "estacionar":
            tipo = args [1]
            id = args[2]
            if tipo == "bike":
                estacionamento.entrar(Bike(id))
            elif tipo == "moto":
                estacionamento.entrar(Moto(id))
            elif tipo == "carro":
                estacionamento.entrar(Carro(id))
        elif cmd == "pagar":
           estacionamento.sair(args[1])
            

if __name__ == "__main__":
    main()         
    
    