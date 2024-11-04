from abc import ABC, abstractmethod

class ComentarioAbstract(ABC):
    def __init__(self, conteudo, autor):
        self.__conteudo = conteudo
        self.__autor = autor
        self.__likes = []

    @property
    @abstractmethod
    def conteudo(self):
        pass

    @conteudo.setter
    @abstractmethod
    def conteudo(self, novo_conteudo):
        pass


    @property
    @abstractmethod
    def autor(self):
        pass

    @property
    @abstractmethod
    def likes(self):
        pass

    @property
    @abstractmethod
    def count_likes(self):
        pass

