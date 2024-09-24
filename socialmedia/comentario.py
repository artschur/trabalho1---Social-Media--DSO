from like import Like


class Comentario:
    def __init__(self, conteudo: str, autor):

        self.__conteudo = conteudo
        self.__autor = autor
        self.__likes = []
        self.__horario_postado = None

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

    @property
    def autor(self):
        return self.__autor

    def receber_like(self, like: Like):
        assert isinstance(like, Like)
        self.__likes.append(like)
