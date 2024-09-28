import comentario


class Post:
    def __init__(self, conteudo: str, autor):
        self.__conteudo = conteudo
        self.__likes = []  # Um post pode ter muitos likes
        self.__comentarios = []
        self.__autor = autor

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
    def comentarios(self):
        return self.__comentarios

    @property
    def autor(self):
        return self.__autor

    def receber_like(self, like):
        self.likes.append(like)

    def adicionar_comentario(self, conteudo, autor):

        self.comentarios.append(comentario.Comentario(conteudo=conteudo, autor=autor))

    def count_likes(self):
        return len(self.__likes)

    def count_comentarios(self):
        return len(self.__comentarios)
