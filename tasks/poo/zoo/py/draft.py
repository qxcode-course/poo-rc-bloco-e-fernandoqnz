from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str) -> None:
        self.__nome = nome

    def showName(self):
        print(f"Eu sou um(a) {type(self).__name__} chamado(a) {self._Animal__nome}")


    @abstractmethod
    def mov(self):
        pass

    @abstractmethod
    def sound(self):
        pass
    
class Leao(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    
    def sound(self):
        print("Ruuuuuuuu")

    def mov(self):
        print("o Leão corre")

class Cobra(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    
    def sound(self):
        print("xiiii")

    def mov(self):
        print("a cobra rasteja")

class Elefante(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def sound(self):
        print("Pruuuuuuuuuuu")

    def mov(self):
        print(" o elefante anda pesado pela floresta")



def apresentar(animal:Animal):
        animal.showName()
        animal.sound()
        animal.mov()
        print(type(animal).__name__)

leao = Leao("simba")
cobra = Cobra("cobrazildo")
elefante = Elefante ("trombis")

lista_animais = [leao, cobra, elefante]

for animal in lista_animais:
    apresentar(animal)
