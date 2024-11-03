from abc import ABC, abstractmethod

class Modelo(ABC):
    def __init__(self, autor):
        self.__autor = autor

    @property
    def autor(self):
        return self.__autor
