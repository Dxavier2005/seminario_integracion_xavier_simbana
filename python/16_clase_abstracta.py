from abc import ABC, abstractmethod


class Catequizando(ABC):
    @abstractmethod
    def asistir(self):
        pass


class CatequizandoComunion(Catequizando):
    def asistir(self):
        print("Asiste a la clase de Primera Comunión")

maria = CatequizandoComunion()
print(maria.asistir)