from abc import ABC, abstractmethod
from datetime import datetime


class Pay(ABC):
    def __init__(self, value:float, desc:str):
        self.value=value
        self.desc=desc


    def res(self):
        print(f"Pagamento de R${self.value}: {self.desc}")
    

    def valueVal(self):
        try :
            if self.value <=0:
                print("valor invalido, digite um valor valido")
        except Exception as e:
            print(e)

    @abstractmethod
    def process(self):
        pass

class Cardcredit(Pay):
    def __init__(self, value: float, desc: str, number:int, nametitular:str, limit:float):
        super().__init__(value, desc)
        self.number=number
        self.nametitular=nametitular
        self.limit = limit

    def process(self):
        if self.value > self.limit:
            print(f"Erro:  limite indisponìvel no cartão {self.number}")
        else:
            self.limit-=self.value
            print(f"Pagamento aprovado no cartão {self.nametitular}. Limite restante: {self.limit}")

    
class Pix(Pay):
    def __init__(self, value: float, desc: str, key:str,bank:str):
        super().__init__(value, desc)
        self.key=key
        self.bank=bank
    
    def process(self):
        if self.value<=0:
            print("valor invalido")
        else:
            print(f"PIX enviado via {self.bank} usando chave {self.key}")
    
class Boleto(Pay):
    def __init__(self, value: float, desc: str, numbercod:int, venc:int):
        super().__init__(value, desc)
        self.numbercod=numbercod
        self.venc=venc

    def process(self):
        today= datetime.now().day
        if self.value <=0:
            print("valor inválido")
        elif today > self.venc:
            print("o boleto vencido")
        else:
            print(f"Boleto {self.numbercod} pago com sucesso! Vencimento: {self.venc}")

def process_pay(pay:Pay):
        pay.valueVal()
        pay.res()
        pay.process()

pix = Pix(
    150,
    "camisa esportiva",
    "fernando@gmail.com",
    "Banco UFC"
)

cartao = Cardcredit(
    400,
    "tenis",
    74229490524542,
    "Fernando Castro",
    500
)

boleto = Boleto(
    89.90,
    "Livro",
    123456789000,
    10
)


pagamentos =[pix, cartao, boleto]

#for p in pagamentos:
#    process_pay(p)
#    print()



    
