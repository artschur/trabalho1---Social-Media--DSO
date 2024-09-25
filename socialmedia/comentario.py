from like import Like
from datetime import datetime


class Comentario:
    def __init__(self, conteudo: str, autor):

        self.__conteudo = conteudo
        self.__autor = autor
        self.__likes = []
        self.__horario_postado = datetime.now()

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

    @property
    def likes(self):
        return self.__likes

    @property
    def horario_postado(self):
        return self.__horario_postado

    @property
    def autor(self):
        return self.__autor

    def receber_like(self, like: Like):
        assert isinstance(like, Like)
        self.__likes.append(like)

    def count_likes(self):
        return len(self.__likes)
