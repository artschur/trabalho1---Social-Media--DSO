from abc import ABC, abstractmethod

class Modelo(ABC):
    def __init__(self, autor):
        self._autor = autor

    @property
    def autor(self):
        return self._autor
    
    @abstractmethod
    def exibir_detalhes(self):
        pass

    @abstractmethod
    def validar(self):
        pass